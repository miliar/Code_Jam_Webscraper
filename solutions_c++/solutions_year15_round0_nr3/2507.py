#include <iostream>
#include <fstream>
#include <vector>
#include <numeric>

enum class quat {
    One,
    I,
    J,
    K,
    MOne,
    MI,
    MJ,
    MK
};

quat toggle(quat x) {
    switch (x) {
        case quat::One: return quat::MOne;
        case quat::I: return quat::MI;
        case quat::J: return quat::MJ;
        case quat::K: return quat::MK;
        case quat::MI: return quat::I;
        case quat::MJ: return quat::J;
        case quat::MK: return quat::K;
        default: return quat::One;
    }
}

bool is_negative(quat x) {
    switch (x) {
        case quat::MOne: return true;
        case quat::MI: return true;
        case quat::MJ: return true;
        case quat::MK: return true;
        default: return false;
    }
}

quat mult(quat a, quat b) {
    if (is_negative(a) && is_negative(b)) {
        return mult(toggle(a), toggle(b));
    }

    if (is_negative(a)) {
        return toggle(mult(toggle(a), b));
    }

    if (is_negative(b)) {
        return toggle(mult(a, toggle(b)));
    }
    
    switch (a) {
        case quat::One:
            return b;
        case quat::I:
            switch (b) {
                case quat::I: return quat::MOne;
                case quat::J: return quat::K;
                case quat::K: return quat::MJ;
                default: return quat::I;
            }
        case quat::J:
            switch (b) {
                case quat::I: return quat::MK;
                case quat::J: return quat::MOne;
                case quat::K: return quat::I;
                default: return quat::J;
            }
        case quat::K:
            switch (b) {
                case quat::I: return quat::J;
                case quat::J: return quat::MI;
                case quat::K: return quat::MOne;
                default: return quat::K;
            }
    }
}

quat to_quat(const char x) {
    if (x == 'i') return quat::I;
    else if (x == 'j') return quat::J;
    else if (x == 'k') return quat::K;
}

quat sum(const std::vector<quat>& v, size_t from, size_t to) {
    quat s = quat::One;
    for (size_t i = from; i < to; ++i) {
        s = mult(s, v[i]);
    }
    return s;
}

void collect_indices(const std::vector<quat>& in, const quat a, const quat b, 
        const size_t from, const size_t to,
        std::vector<size_t>& ra, std::vector<size_t>& rb) {
    std::vector<size_t> r;
    quat left = quat::One;
    quat right = quat::One;

    for (size_t l = from, r = to; l < to; ++l, --r) {
        left = mult(left, in[l]);
        right = mult(in[r], right);

        if (left == a)
            ra.push_back(l);
        if (right == b)
            rb.push_back(r);
    }

}

bool solve(std::vector<quat> testcase) {
    if (testcase.size() < 3)
    {
        return false;
    }

    quat i = quat::One;
    quat k = quat::One;

    std::vector<size_t> candidates_a, candidates_b;
    collect_indices(testcase, quat::I, quat::K, 0, testcase.size() - 1, candidates_a, candidates_b);

    for (size_t x = 0; x < candidates_a.size(); ++x) {
        quat j = quat::One;
        size_t last_index = candidates_a[x] + 1;
        for (size_t y = 0; y < candidates_b.size(); ++y) {
            quat s = sum(testcase, last_index, candidates_b[y]);
            j = mult(j, s);

            last_index = candidates_b[y];

           if (j == quat::J)
              return true; 
        }
    }

    return false;
}


int main(int argc, char** argv) {
    std::ifstream ifs;

    ifs.open(argv[1], std::ifstream::in);

    size_t num_testcases = 0;
    ifs >> num_testcases;

    std::vector<std::vector<quat> > testcases;
    

    for (size_t i = 0; i < num_testcases; ++i) {
        size_t size = 0;
        size_t mult = 0;
        ifs >> size;
        ifs >> mult;
        testcases.push_back(std::vector<quat>());

        std::vector<quat> tmp;
        for (size_t j = 0; j < size; ++j) {
            char t = 0;
            ifs >> t;
            tmp.push_back(to_quat(t));
        }

        if (tmp.size() <= 1)
            continue;

        for (size_t j = 0; j < mult; ++j) {
            testcases[i].insert(testcases[i].end(), tmp.begin(), tmp.end());
        }
    }

    for (size_t i = 0; i < testcases.size(); ++i) {
        std::cout << "Case #" << (i + 1) << ": ";

        bool result = solve(testcases[i]);
        if (result)
            std::cout << "YES" << std::endl;
        else 
            std::cout << "NO" << std::endl;
    }
}
