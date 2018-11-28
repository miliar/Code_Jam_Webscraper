#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <map>

using namespace std;


int main() {
    int zc;
    cin>>zc;
    for(int tc=1;tc<=zc;tc++)
    {
        int result,R,C,W;
        cin>>R>>C>>W;

        result = R*C/W + W - ((C%W)?0:1);

        cout<<"Case #"<<tc<<": "<<result<<endl;
    }
}


