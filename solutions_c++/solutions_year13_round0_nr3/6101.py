#include <string>
#include <vector>
#include <map>

#include <stdio.h>
#include <stdlib.h>

#include <sstream>
#include <iostream>
#include <utility>

//uses gmplib
#include <gmpxx.h>

using std::string;
using std::vector;

typedef mpz_class big_int;
typedef std::pair<big_int,big_int> range;
typedef vector<range> range_vector;
typedef std::map<big_int,bool> cache;

string get_line(std::vector<char>::iterator &it) {
    vector<char> vline;
    
    char symbol = '\n';

    symbol = *it;

    while (symbol != '\n') {
        vline.push_back(symbol);
        it++;
        symbol = *it;
    };

    it++;

    string sline(vline.data());
    return sline;
}

range parse_range(string line) {
    big_int i = 0;
    big_int j = 0; 

    std::stringstream ss(line);
    string first, second;

    //break on space
    std::getline(ss, first, '\040');
    std::getline(ss, second);

    i = std::stoi(first);
    j = std::stoi(second);

    range rang(i,j);
    return rang; 
}

range_vector * parse_input(vector<char> * input) {
    range_vector * all_ranges = new range_vector();

    vector<char>::iterator it = input->begin();
    
    get_line(it);

    string line;
    range rang;

    while (it != input->end()) {
        line = get_line(it);
        rang = parse_range(line);
        all_ranges->push_back(rang);
    }

    return all_ranges;
}


big_int get_perfect_root(big_int &number) {
    mpz_t root;
    mpz_init(root);

    if (mpz_root(root, number.get_mpz_t(), 2) != 0) {
        return big_int(root);
    } else {
        return big_int(-1);
    }
}

bool is_square(big_int &number) {
    mpz_t root;
    mpz_init(root);

    if( mpz_root(root, number.get_mpz_t(), 2) != 0) {
        return true;
    } else { 
        return false;
    }
}

bool is_palindrome(big_int &number) {
    bool flag = true;

    string as_string = number.get_str();
    //std::cout << as_string << std::endl;

    int length = as_string.length() - 1;

    for( int i = 0; (i <= length - i) && (flag == true); i++) {
        if (as_string[i] != as_string[length - i]) {
            flag = false;
        }
    }

    return flag;
}

// calculate fair and square
bool calculate_fns(big_int &i) {
    if(is_square(i)) {
        if(is_palindrome(i)) {
            return true; 
        } else {
            return false;
        }
    } else {
        return false;
    }
}

cache * calculate_cache(big_int begin, big_int end) {
    cache * cache_data = new cache();
    
    cache_data->insert(std::pair<big_int,bool>(1,true));

    for (big_int i = begin; i <= end; i++) {
        bool is_fns = true;

        //std::cout << "fns " << calculate_fns(i) << " ";
        if (calculate_fns(i) == true) {
            big_int root = get_perfect_root(i);
            //std::cout << "root" << root << " ";
            if (is_palindrome(root) == true) {
                //is_fns = cache_data->at(root);
            } else {
                is_fns = false;
            }
        } else {
            is_fns = false;
        }
        
        if (is_fns) {
            cache_data->insert(std::pair<big_int,bool>(i,true));
        }
        //std::cout << i.get_str() << " : " << cache_data->at(i) << "\n";
    }
        

/*        big_int root = get_root(i);
        if(cache_data->find(root) != cache_data->end()) {
            bool is_fns = (calculate_fns(i) && cache_data->at(root));
            cache_data->insert(std::pair<big_int,bool>(i,is_fns));
        } else {
            cache_data->insert(std::pair<big_int,bool>(i,false));
        }

        std::cout << i.get_str() << " : " << calculate_fns(i) << "\n";

    };
*/
    return cache_data;
}

big_int num_fns_in_range(range rng, cache * cache_data) {
    big_int total = 0;

    for (big_int i = rng.first; i <= rng.second; i++) {
        if ( cache_data->find(i) != cache_data->end() ) {
            total++;
        }
    }

    return total;
}


int main() {
    char buffer[128];
    size_t bytes_read = 0;
    int bytes_read_total = 0;

    vector<char> * input = new vector<char>();

    while((bytes_read = fread(buffer, 1, sizeof(buffer), stdin)) > 0) {
        input->insert(input->end(), buffer, buffer+bytes_read);
        bytes_read_total += bytes_read;
    }


    range_vector * all_ranges = parse_input(input);

    mpz_t upper_limit;
    mpz_init(upper_limit);

    mpz_pow_ui(upper_limit,big_int(10).get_mpz_t(),6);

    cache * cache_data = calculate_cache(1,big_int(upper_limit));

    big_int count = 1;

    for (range_vector::iterator it = all_ranges->begin(); it != all_ranges->end(); ++it) {

        std::cout << "Case #" << count << ": " << num_fns_in_range(*it,cache_data) << "\n";

        count++;
    }
    return 0;
}

