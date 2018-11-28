#include <iostream>
#include <iostream>
#include <fstream>
#include <vector>
#include <cstring>
#include <sstream>
#include <algorithm>
#include <cmath>
using namespace std;
#define lli long long
int d1,d2;
lli reverseit(lli i)
{
    lli out;
    char buf[20];
    sprintf(buf,"%lld",i);
    d1=strlen(buf);
   // cout<<buf<<'\n';
    reverse(buf,buf+strlen(buf));
    stringstream ss;
    ss<<buf;
    ss>>out;
    sprintf(buf,"%lld",out);
    d2=strlen(buf);
    return out;
}
lli cur_min;
lli find_out(lli N_now,lli N)
{
    /*
   // cout<<N_now<<" "<<N<<" "<<cur_min<<endl;
    if(cur_min<N)
        return cur_min;
    if(N_now<=19)
    {
        if(cur_min>N+N_now)
        {
            cur_min=N+N_now;
        }
       // cout<<N_now<<"*"<<N<<endl;
        return N+N_now;
    }
    else
    {
        lli r=reverseit(N_now);
        while(d1!=d2){
            while(N_now<reverseit(N_now))
            {
                N_now--;
                N++;
            }
            if(d1!=d2){
                N_now--;
                N++;
                reverseit(N_now);
            }

        }
        return find_out(reverseit(N_now),N+1);

    }
    */
    if(N_now<19)
        return N_now;
    lli o=1;
    do{
        //cout<<o<<'\n';
        N++;
        lli r=reverseit(o);
        if(o<r)
        {
            if(r<=N_now){
                o=r;
                continue;
            }
            else{
                o++;
            }
        }
        else
        {
            o++;
        }
    }while(N_now!=o);
    return N+1;
}
int main()
{
    ifstream in("A-small-attempt2.in");
    ofstream out("A-small.out");
#define cin in
#define cout out
 //   cout<<reverseit(123456)<<"!!!"<<endl;

    static int mas[10000000];
    for(int i=0;i<=20;i++)
    {
        mas[i]=i;
    }
    for(int i=21;i<=1000000;i++)
    {
        int ir=reverseit(i);
        if(ir>=i){
                //cout<<i<<" "<<ir<<endl;
            mas[i]=mas[i-1]+1;
        }
        else
        {
            if(d1==d2)
            {
                //cout<<" d1==d2 "<<i<<" "<<ir<<endl;
                 mas[i]=min(mas[i-1],mas[ir])+1;
            }
            else
            {
               // cout<<" d1!d2 "<<i<<" "<<ir<<endl;

                mas[i]=mas[i-1]+1;
            }
        }
        //cout<<mas[i]<<endl;
    }
   /* for(int i=0;i<24;i++)
    {
        cout<<mas[i]<<" ";
    }*/
    int T;
    cin>>T;
    for(int iT=0; iT<T; iT++)
    {
        cur_min=1e15;
        long long N;
        cin>>N;
        printf("%i\n",iT+1);

        cout<<"Case #"<<iT+1<<": "<<mas[N]<<endl;
    }
    return 0;
}
