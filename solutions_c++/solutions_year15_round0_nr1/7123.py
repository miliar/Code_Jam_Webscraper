
#include <iostream>
using namespace std;

int main() {
    int tcs,smax;
    string s;
    cin >> tcs;
    for(int y =1; y< tcs+1; ++y)
    {
        cin >> smax >> s;
        //cout<< smax << " " << s;
        int count = s[0] - '0';
        int need = 0;
        for (int i=1;i< smax+1;++i)
        {
            int t = s[i] - '0';
            if (t == 0)
                continue;
            if(i>count)
                need += i-count;
            count+= t + i-count;
        }
        cout<< "Case #"<<y<<": "<<need<<endl;
    }
    return 0;
}
