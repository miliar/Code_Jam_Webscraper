#include<iostream>
using namespace std;






main()
{
    ios_base::sync_with_stdio(0);

    int T;
    cin >> T;

    for(int asd=1; asd<=T; ++asd)
    {
        int n=asd;
        cin >> n;

        bool seen[10];
        for(int i=0; i<10; ++i) seen[i]=false;

        int num=n;
        bool insomnia=true;
        for(int i=1; i<=500; ++i)
        {
            int tmp=num;


            while(tmp>0)
            {
                seen[tmp%10]=true;
                tmp/=10;
            }

            bool all=true;
            for(int j=0; j<10; ++j) if(!seen[j]) all=false;

            if(all)
            {
                insomnia=false;
                break;
            }

            num+=n;
        }

        if(!insomnia) cout << "Case #" << asd << ": " << num << endl;
        else cout << "Case #" << asd << ": INSOMNIA" << endl;
    }



    return 0;
}
