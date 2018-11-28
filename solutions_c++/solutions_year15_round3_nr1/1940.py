#include <iostream>
#include <fstream>

using namespace std;


int main()
{
    int T,t;
    cin>>T;
    for(t=0;t<T;t++){
     int r,c,w;
     cin>>r;
     cin>>c;
     cin>>w;
     int h=0,tmp;
     int i,j;
     for(i=w-1,j=1; i<c; i=i+w, j++){
        tmp=j;
        if(i+1>=c) tmp+=w-1;
        else tmp+=w;
        if(tmp>h) h=tmp;
     }
     cout<<"Case #"<<t+1<<": "<<h<<endl;
    }
    return 0;
}

