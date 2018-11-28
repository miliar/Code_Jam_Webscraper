#include<iostream>
#include<set>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;

int main(void)
{
    int T;
    cin >> T;
    for(int Ti=0; Ti<T; ++Ti)
    {
        int Smax;
        cin >> Smax;
        string S;
        cin >> S;
        int add = 0;
        int tot = 0;
        for(int i=0; i<=Smax; ++i)
        {
            int si = ((int)S[i])-48;
            int newAdd = 0;
            if(si>0){
                if(i>tot)
                {
                    newAdd = (i-tot);
                    add+=newAdd;
                    tot+=(newAdd+si);
                }
                else
                {
                    tot+=si;
                }
            }
        }
        cout << "Case #" << (Ti+1) << ": " << add << endl;
    }

	return 1;
}