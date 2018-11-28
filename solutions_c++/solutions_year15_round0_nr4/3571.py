#include<iostream>
#include<algorithm>
#include<fstream>
using namespace std;
int main()
{
    ofstream outfile;
    ifstream infile;
    outfile.open("d1.out");
    infile.open("D-small-attempt0.in");
    int t;
    infile >> t;
    //cin>>t;
    for(int i=0;i<t;i++)
    {
        int x,r,c;
        infile >> x;
        infile >> r;
        infile >> c;
        if((r*c)%x!=0){
            outfile<<"Case #"<<i+1<<": RICHARD"<<endl;
        }
        else{
            int min;
            if(r>c)
                min=c;
            else
                min=r;
            if((min+1)<=x){
                if((min+1)==x &&(((x==r && x==(c+1))||(x==c && x==(r+1)))||(r%c==0 || c%r==0))){
                outfile<<"Case #"<<i+1<<": GABRIEL"<<endl;
                //cout<<"Y"<<endl;
                }
                else
                outfile<<"Case #"<<i+1<<": RICHARD"<<endl;
            }
            else if((min+1)>x)
            outfile<<"Case #"<<i+1<<": GABRIEL"<<endl;
        }
    }
    return 0;
}
