#include<math.h>
#include<algorithm>
#include<iostream>
#include<cstdio>
#include<stdlib.h>
#include<string.h>
#include<vector>

using namespace std;
main()
{

//    freopen("input.txt","r",stdin);
    //1freopen("output.txt","w",stdout);

    int T,T_i;
    cin>>T;
    for(T_i = 0; T_i < T; T_i++)
    {
        int n1,n2,hash[17] = {},num,count = 0;

        cin>>n1;
        for(int i = 1; i <= 4; i++)
        {
            int a,b,c,d;
            cin>>a>>b>>c>>d;
            if( i == n1)
            {
                hash[a]++;
                hash[b]++;
                hash[c]++;
                hash[d]++;
            }
        }

        cin>>n2;
        for(int i = 1; i <= 4; i++)
        {
            int a,b,c,d;
            cin>>a>>b>>c>>d;
            if( i == n2)
            {
                if(hash[a]) {count++; num = a;}
                if(hash[b]) {count++; num = b;}
                if(hash[c]) {count++; num = c;}
                if(hash[d]) {count++; num = d;}
            }
        }

        cout<<"Case #"<<T_i+1<<": ";
        if(count == 1)  cout<<num<<endl;
        else if(count > 1) cout<<"Bad magician!"<<endl;
        else cout<<"Volunteer cheated!"<<endl;
    }

    return 0;
}
