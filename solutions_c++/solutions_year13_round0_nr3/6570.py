#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int reverse(int a){
    int n,b;
    n = 0;
    while(a > 0){
        b = a/10;
        b = b*10;
        n = n*10;
        if(b > 0)n = n + (a % b);
        else n = n + a;
        a = a/10;
    }
    return n;
}

int main()
{
    ifstream h;
    h.open("input.in");
    int eil[10] = {1,2,10,11,20,100,101,110,111,200};
    int t,j,a = 1,b = 1,c,d;
    h >> t;
    vector <int> sk;
    sk.push_back(1);
    sk.push_back(2);
    sk.push_back(3);
    for(int y = 0;y<10;y++){
        b = 1;
        a = eil[y];
        while(a > 0){
            a /= 10;
            b *= 10;
        }
        sk.push_back((eil[y]*b) + reverse(eil[y]));
        sk.push_back((eil[y]*(b*10)) + reverse(eil[y]));
        sk.push_back((eil[y]*(b*10)) + b*1 + reverse(eil[y]));
        if((eil[y] != 111) && (eil[y] != 2) && (eil[y] != 20) && (eil[y] != 200)) sk.push_back((eil[y]*(b*10)) + b*2 + reverse(eil[y]));
    }
    sort(sk.begin(),sk.end());
    freopen("output.out","w",stdout);
    for(int y = 0;y<t;y++){
        h >> a >> b;
        d = 0;
        for(int i = 0;i<sk.size();i++){
            if((sk[i]*sk[i] >= a)&&(sk[i]*sk[i] <=b)){
                 d++;
            }
        }
        cout << "Case #" << y + 1 << ": " << d << endl;
    }

    return 0;
}
