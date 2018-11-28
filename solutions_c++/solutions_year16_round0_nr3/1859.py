#include <algorithm>
#include <array>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <vector>

#include <gmpxx.h>

static std::vector<unsigned> found_bitfields;
const static std::array<int, 169> common_primes = {
    1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
    79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167,
    173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263,
    269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367,
    373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
    467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587,
    593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683,
    691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811,
    821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929,
    937, 941, 947, 953, 967, 971, 977, 983, 991, 997
};

struct SuccessCase {
    unsigned bitfield;
    std::array<int, 9> dividends;
};

mpz_class base2_as(unsigned bitfield, unsigned base) {
    if (base == 2)
        return bitfield;

    mpz_class num;
    for (int i = sizeof(bitfield) * 8 - 1; i >= 0; i--) {
        mpz_class powd;
        if (bitfield & (1 << i)) {
            mpz_pow_ui(powd.get_mpz_t(), mpz_class(base).get_mpz_t(), i);
        }
        num += powd;
    }
    return num;
}

int find_dividend(mpz_class num) {
    std::string num_s = num.get_str().c_str();
    for (int i : common_primes) {
        if (num % i == 0 && i != 1 && num != i)
            return i;
    }
    return 0;
}

std::vector<SuccessCase> test_with_base(unsigned base, int size, int max_nums) {
    std::vector<SuccessCase> ret;

    for (int prime : common_primes) {
        if (max_nums == 0)
            break;

        unsigned new_num = base * prime;
        if (32 - __builtin_clz(new_num) > size - 2)
            break;

        SuccessCase scase = {
            .bitfield = (1 << (size - 1)) | 1 | new_num << 1,
            .dividends = {},
        };

        for (int i = 2; i <= 10; i++) {
            int dividend = find_dividend(base2_as(scase.bitfield, i));
            if (dividend == 0)
                goto next_prime;
            
            scase.dividends[i - 2] = dividend;
        }
        
        {
            // Check if already found
            auto found_pos = std::lower_bound(found_bitfields.begin(), found_bitfields.end(), scase.bitfield);
            if (found_pos != found_bitfields.end() && *found_pos == scase.bitfield)
                goto next_prime;
            found_bitfields.insert(found_pos, scase.bitfield);
        }
        
        ret.push_back(scase);
        max_nums--;
next_prime: ;
    }

    return ret;
}

std::vector<SuccessCase> test_all(int size, int nums) {
    std::vector<SuccessCase> scases;
    
    for (int prime : common_primes) {
        if (nums == 0)
            break;
        
        std::vector<SuccessCase> new_cases = test_with_base(prime, size, nums);
        nums -= new_cases.size();
        scases.insert(scases.end(), new_cases.begin(), new_cases.end());
    }
    assert(nums == 0);
    return scases;
}

int main(int argc, char** argv) {
    int num_cases = 0;
    int size = 0;
    int nums = 0;

    scanf("%d", &num_cases);
    assert(num_cases = 1);
    
    scanf("%d %d", &size, &nums);
    
    std::vector<SuccessCase> scases = test_all(size, nums);

    printf("Case #1:\n");
    for (auto scase : scases) {
        for (int i = 32 - __builtin_clz(scase.bitfield) - 1; i >= 0; i--) {
            printf("%d", scase.bitfield >> i & 1);
        }

        for (unsigned dividend : scase.dividends) {
            printf(" %d", dividend);
        }
        printf("\n");
    }
}