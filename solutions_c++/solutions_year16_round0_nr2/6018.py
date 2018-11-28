//================================================================================================//
//  problem2.h
//  GoogleCodeJam
//
//  Created by Zachary Clawson on 4/9/16.
//  Copyright © 2016 Zachary_Clawson. All rights reserved.
//================================================================================================//

#ifndef problem2_h
#define problem2_h

/* Google Code Jam [April 8, 2016], Problem 2: Revenge of the pancakes
 *
 */

namespace date_2016_04_08 {
namespace problem2 {

//------------------------------------------------------------------------------------------------//
//------------------------------------------------------------------------------------------------//

const std::string working_dir = "/Users/zacharyclawson/Desktop/Code/GoogleCodeJam/GoogleCodeJam/2016_04_08/";

//------------------------------------------------------------------------------------------------//
//------------------------------------------------------------------------------------------------//

inline
bool vector_all_elements_true(const std::vector<bool> & v) {
    const bool all_true = std::all_of(std::begin(v),
                    std::end(v),
                    [](bool i)
                    {
                        return i; // or return !i ;
                    });
    return all_true;
}

//------------------------------------------------------------------------------------------------//
//------------------------------------------------------------------------------------------------//

inline
int number_of_sign_changes(const std::string & s) {
    int sign_changes = 0;
    
    char last_c = s.at(0);
    
    for (int i = 1; i < s.length(); ++i) {
        char c = s.at(i);
        if (c != last_c) {
            ++ sign_changes;
        }
        last_c = c;
//        std::cout << c << std::endl;
    }
    return sign_changes;
}

//------------------------------------------------------------------------------------------------//
//------------------------------------------------------------------------------------------------//

/** Runner for this problem.
 *
 */
void run_problem() {
    //-- Problem info ----------------------------------------------------------------------------//
    std::cout << "Doing problem B." << std::endl << std::endl;;
    
    //-- Inputs ----------------------------------------------------------------------------------//
//    const std::string filename = working_dir + "data/problem2_easy.txt";
    const std::string filename = working_dir + "data/problem2_hard.txt";
    const auto pancakes = io::read_data_to_vector_array2d<std::string>(filename);
    
    //-- Constants -------------------------------------------------------------------------------//
    const int number_of_cases = std::stoi(pancakes[0]);
    
    //-- File writing ----------------------------------------------------------------------------//
    std::ofstream results_file;
//    results_file.open(working_dir + "problem2_easy_results.txt");
    results_file.open(working_dir + "problem2_hard_results.txt");

    //-- Main loop -------------------------------------------------------------------------------//
    int case_counter = -1;
    for (std::string pancake : pancakes) {
        // Skip the first line:
        if (case_counter == -1) {
            ++ case_counter;
            continue;
        }
        
        // Increment which case we're in:
        ++ case_counter;
        
        int flip_counter = number_of_sign_changes(pancake);
        
        // if bottom pancake is '-', we need to have 1 extra flip:
        if (pancake[pancake.length() - 1] == '-') ++ flip_counter;
        
        /*
        
        std::vector<bool> pancake_happy(pancake.length(), false);
        int p_id = 0;
        for ( auto p : pancake ) {
            if (p == '+') {
                pancake_happy[p_id] = true;
            } else {
                assert(p == '-');
            }
            ++ p_id;
        }
        
        // Counters
        int flip_counter = 0;
        
        bool done = vector_all_elements_true(pancake_happy);
        
        while ( ! done ) {
            ++ flip_counter;
            
            
            
            done = vector_all_elements_true(pancake_happy);
        }
        */
        
        // Output
        std::cout << pancake << std::endl;
        results_file << "Case #" << case_counter << ": " << flip_counter;
//        std::cout << "Case #" << case_counter << ": " << flip_counter << std::endl;
        if (case_counter != number_of_cases) {
            results_file << std::endl;
        }
    }
    
    assert(case_counter == number_of_cases);
    
    //-- File writing ----------------------------------------------------------------------------//
    results_file.close();
}

//------------------------------------------------------------------------------------------------//
//------------------------------------------------------------------------------------------------//

} // problem2
} // namespace date_2016_04_08

#endif /* problem2_h */
