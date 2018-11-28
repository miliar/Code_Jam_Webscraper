#include "CodeJam.hpp"
#include "Pancake2.hpp"

int Pancake2::solveAll() {
    int testCases;
    readln(testCases);
    
    for (curCase = 1; curCase <= testCases; ++curCase) {
        std::cout << "Test " << curCase << " of " << testCases << std::endl;
        solve(curCase);
    };
    return testCases;
}


void Pancake2::solve(int task) {
    
    readln(S);
    int sum = 0, pos = 0, cnt=0;
    bool done = false;
    
    done = check();
    char burnt='+';
    for(int i = S.size()-1; i>=0; i--) {
        if(S[i]!=burnt) {
            cnt++;
            burnt = burnt == '+' ? '-' : '+';
        }
    }
    
    
    std::cout << cnt;
    
    std::cout << std::endl;
    /*if(N==0) {
        writeResult("INSOMNIA");
    } else {
        int done=0;
        int c=0;
        while(!done){
            c++;
            int w = c * N;
            std::ostringstream os;
            
            os << w;
            std::string digits = os.str();
            for(std::string::size_type i = 0; i < digits.size(); ++i) {
                nums[std::stoi(digits.substr(i,1))]=1;
            }
            
            if(10==std::accumulate(begin(nums), end(nums), 0, std::plus<int>())) {
                done = true;
                writeResult(c*N);
            }
        }
    }*/
    writeResult(cnt);
}

int Pancake2::count(int task) {
    return task;
}

bool Pancake2::check() {
    for(int i = 0; i <= S.size(); i++) {
        if(S[i]=='-') {
            return false;
        }
    }
    return true;
}
/*
 var A = Array(1, 0, 1, 0, 0, 1, 0, 1);
 var sum = 0;
 
 // count the 1s in the original array and
 // do the 0 -> 1 and 1 -> -1 conversion
 for(var i = 0; i < A.length; i++) {
 sum += A[i];
 A[i] = A[i] == 0 ? 1 : -1;
 }
 
 // find the maximum subarray
 var x = { value: 0, left: 0, right: 0 };
 var y = { value: 0, left: 0 };
 for (var n = 0; n < A.length; n++) {
 // update y
 if (y.value + A[n] >= 0) {
 y.value += A[n];
 } else {
 y.left = n+1;
 y.value = 0;
 }
 // update x
 if (x.value < y.value) {
 x.left = y.left;
 x.right = n;
 x.value = y.value;
 }
 }
 
 // convert the result back
 alert("result = " + (sum + x.value)
 + " in range [" + x.left + ", " + x.right + "]");
*/