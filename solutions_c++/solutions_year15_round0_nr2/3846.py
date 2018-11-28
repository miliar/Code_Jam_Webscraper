#include <iostream>
#include <fstream>
#include <stdio.h>
#include <cstring>
#include <algorithm>
using namespace std;
const int BUF_SIZE=100;
bool comp(int a,int b)
{
    return (a>b);
}
int MIN_ANS=10;
void do_one( int const*buf,int col,int depth)
{
  //  ofstream out("try.txt",ios::ate|ios::app);
//#define cout out2
    int buf_mine[BUF_SIZE];
    memcpy(buf_mine,buf,col*sizeof(int));
    //sort(buf_mine,buf_mine+all,comp);
    if(depth>MIN_ANS)
        return;
   /* for(int i=0; i<depth; i++)out<<" ";
    out<<"depth="<<depth<<"\n";
    for(int i=0; i<depth; i++)out<<" ";
    for(int i=0; i<col; i++)
    {
        out<<buf_mine[i]<<" ";
    }
    out<<endl;*/
    if(buf_mine[0]<=0)
    {
        if(depth==6)
        {
            /*out<<"!!!*******\n";
            for(int i=0; i<depth; i++)out<<" ";
            for(int i=0; i<col; i++)
            {
                out<<buf_mine[i]<<" ";
            }*/
        }
        if(MIN_ANS>depth)
            MIN_ANS=depth;
        return;
    }
    int prev=buf_mine[0];
//for(int i=0;i<col;i)
    for(int i=1; i<prev/2+1; i++)
    {

        int buf_mine2[BUF_SIZE];
        memcpy(buf_mine2,buf_mine,col*sizeof(int));
        buf_mine2[0]=prev-i;
        buf_mine2[col]=i;
        sort(buf_mine2,buf_mine2+col+1,comp);
        //cout<<"generating -- "<<buf_mine[0]<<" "<<buf_mine[col]
        do_one(buf_mine2,col+1,depth+1);
    }

    int buf_mine2[BUF_SIZE];
    memcpy(buf_mine2,buf_mine,col*sizeof(int));
    for(int i=0; i<col; i++)
    {
        buf_mine2[i]--;
        if(buf_mine2[i]<=0)
        {
            col=i;
            break;
        }
    }
    do_one(buf_mine2,col+1,depth+1);

}
int main()
{
    ofstream out("B-small-attempt5.out");
    ifstream in("B-small-attempt5.in");
#define cin in
#define cout out
    int T;
    cin>>T;
    for(int i=0; i<T; i++)
    {
        int buf[1010];
        int N;
        cin>>N;
        int wins=0;
        for(int j=0; j<N; j++)
            cin>>buf[j];
        sort(buf,buf+N,comp);
        MIN_ANS=9;
        do_one(buf,N,0);
        //cout<<do_one(buf,7,9,3);
        cout<<"Case #"<<i+1<<": "<<MIN_ANS<<"\n";
    }
    return 0;
}
