
/**
	You're given two strings, "pattern" and "input", e.g.
 
 pattern: "abba"
 input: "redbluebluered"
 
 This example is considered a match because the pattern of words in input matches the pattern of characters in pattern.
 The pattern specifies that you have an instance of one word, two instances of another word, and another instance
 ofthe first word.
 
 Write a function that takes in a pattern and an input, and determines whether you have a match.
 Return 1 if it is a match, and 0 if it is not a match.
 
 The running time of the algorithm is exponential to the length of the input. Performance isn't too important for this
 question, but the algorithm should be efficient enough to run the provided test cases.
 
 The pattern can contain any characters in any order.
 
 Words must be at least one character long.  The input will be at least as long as the pattern.
 
 Distinct pattern characters must correspond to distinct input words, so e.g. A pattern of "abba" and an input of
 "redredredred" is NOT a match.
 
 SAMPLE CASES:
 1) pattern is "abba", input is "redbluebluered" - should return 1
 2) pattern is "aaaa", input is "redbluebluered" - should return 0
 
 NOTE: The input does not need to contain actual "dictionary words". "abcxyzxyzabc" would also be an input that matches the pattern "abba".
 */

#include <iostream>
#include <unordered_map>
#include <stack>
using namespace std;

const int numToBit[10] = {1,2,4,8,16,32,64,128,256,512};
const int GOAL = 1023; // first 10 bits of an int set to 1 = 1023

int64_t sheepBleatrix(int64_t N){
    int16_t counter = 0;
    // first 10 bits set to 1 = 1023
    int64_t n = N, copy = N, previousCopy= copy;
    int changesToSkip = 10;
    for(size_t i = 2 ; changesToSkip ; ++i){
        previousCopy = copy;
        while (copy){
            counter |= numToBit[copy%10];
            copy /= 10;
        }
        if (counter == GOAL)
            return n;
        
        if (copy == previousCopy){
            // didn't see any new digit.
            --changesToSkip;
        } else {
            // we saw a new digit.
            changesToSkip = 10;
        }
        
        n = N * i;
        copy = n;
    }
    
    return -1;
}

int main() {
    int T;
    int64_t N;
    cin >> T;
    for(int i = 1; i <= T; ++i){
        cin >> N;
        cout << "Case #"<< i <<": ";
        int64_t result = sheepBleatrix(N);
        if (result < 0){
            cout << "INSOMNIA" << endl;
        } else {
            cout << result << endl;
        }
    }
    return 0;
}