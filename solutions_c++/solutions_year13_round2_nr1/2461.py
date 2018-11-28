#include<iostream>
#include<cstdio>
#include<vector>
#include<map>
#include<algorithm>
using namespace std;
#define LL long long
int main()
{
    int test,t=1;
    LL A,N;
    vector<LL> motes;
    LL var;
    cin >> test;
    LL out;
    for(;t<=test;t++)
    {
        motes.clear();
        cout << "Case #"<<t<<": ";
        cin >> A >> N;
        for(int i =0;i<N;i++)
        {
            cin >> var;
            motes.push_back(var);
        }
        sort(motes.begin(),motes.end());
        if(A == 1)
        {
            cout << N <<endl;
            continue;
        }
        LL op=0;
        LL output;
        int i=0;
        bool flag = false;
        while(i<N)
        {
//            cout <<motes[i]<<" "<<A<<endl;
         if(motes[i] >=A)
         {
          //   cout <<"op "<<op<<endl;
             /*if(1 >= N-i)

             {
                 
                 output = op+N-i;
                  cout <<"out "<< output<<endl;
                 flag = true;
                 break;
             }*/
             
             {
                 int temp = op;
        //         cout <<"temp " <<temp <<endl;
                 int cnt = 0;
                 while(motes[i]>= A){
                 cnt++;
                 A+=A-1;
                 }
                 if(cnt >= N-i)
                 {
                     output = temp+N-i;
          
            //      cout <<"output "<< output<<endl;
                     flag= true;
                     break;
                 }
                 else
                 {
                     op+=cnt;
                     
                 }
                 
             }
         }
         else
         {
             A+=motes[i];
             
             i++;
         }
        }
    //    cout << op << " ";
        if(!flag){
        output = op;
        output = min(N,output);
        }
        cout << output<<endl;
    }
    return 0;
}
