#include<iostream>

using namespace std;

int M1[4][4],M2[4][4];
int r1,r2;

int findpos(int n)
{
    for(int i=0;i<4;++i)
    for(int j=0;j<4;++j)
    if(M2[i][j]==n)return i;
}

void do_a_case(int case_no)
{
    int i,j,cnt=0,num=0;
    cin>>r1;
    for(i=0;i<4;++i)
    for(j=0;j<4;++j)
    cin>>M1[i][j];
    cin>>r2;
    for(i=0;i<4;++i)
    for(j=0;j<4;++j)
    cin>>M2[i][j];
    i=r1-1;
    for(j=0;j<4;++j)
    if(findpos(M1[i][j])==r2-1)cnt++,num=M1[i][j];
    if(cnt==1)
    cout<<"Case #"<<case_no<<": "<<num<<"\n";
    else if(cnt==0)
    cout<<"Case #"<<case_no<<": Volunteer cheated!\n";
    else
    cout<<"Case #"<<case_no<<": Bad magician!\n";
    //cout<<cnt<<":"<<num<<endl;

}


int main()
{
    int T;
    cin>>T;
    for(int i=0;i<T;++i)
    do_a_case(i+1);
    return 0;
}
