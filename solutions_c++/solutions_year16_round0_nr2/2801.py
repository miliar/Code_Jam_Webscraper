#include<iostream>
using namespace std;


main()
{
    ios_base::sync_with_stdio(0);
    int z;
    cin >> z;
    for(int asd=1; asd<=z; ++asd)
    {
        string S;
        cin >> S;

        int result=0, n=S.length();

        int tmp=0; bool premin=false;
        while(tmp<n && S[tmp]=='-') {S[tmp++]='+'; premin=true;}
        if(premin) result++;

        //cout << S << endl;
        bool potrzebuje=true;
        while(potrzebuje)
        {
            int it1=0, it2=0;
            while(it1<n && S[it1]=='+') it1++;
            if(it1==n) break;
            it1--;
            it2=it1+1;
            while(it2<n && S[it2]=='-') it2++;
            it2--;
            result+=2;
            for(int i=it2; i>=it1; --i) S[i]='+';

        }

        cout << "Case #" << asd << ": " << result << endl;
    }
    return 0;
}
