#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <iostream>
#include <string.h>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <iostream>
#include <string.h>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <fstream>
#include <unordered_map>
#include <unordered_set>

using namespace std;

int main(){
    ifstream in("/Users/tech8/Desktop/Ainput.txt");
    ofstream out("/Users/tech8/Desktop/Aoutput.txt");

    long long testcase;
    in >> testcase;
    for(int s = 0; s < testcase; s++)
    {
        string text;
        in >> text;
        string temp;
        temp.push_back(text[0]);
        for(int i = 1; i < text.length(); i++){
            string h;
            h.push_back(text[i]);
            string left = "";
            left = h;
            left = left + temp;
            string right = "";
            right = temp + h;
            if(right < left){
                temp = left;
            }else {
                temp = right;
            }
        }
        out << "Case #" << s + 1 << ": " << temp << endl;
    }
}