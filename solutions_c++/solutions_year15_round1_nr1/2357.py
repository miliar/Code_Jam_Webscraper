#include <iostream>
#include <fstream>
#include <vector>

using namespace std;


int main()
{
    ifstream input("A.in");
    string const out("A.out");
    ofstream output(out.c_str());

    int s,i,a,j,t1,t2,k;

    input>>s;
    for(i=1;i<=s;i++){
        input>>a;
        int T[a];
        for(j=0;j<a;j++)input>>T[j];
        t1=0;
        for(j=1;j<a;j++){
            if((T[j-1]-T[j])>=0) t1=t1+T[j-1]-T[j];
        }
        k=T[0]-T[1];
        t2=0;
        for(j=1;j<a;j++)if((T[j-1]-T[j])>k) k=T[j-1]-T[j];
        for(j=0;j<a-1;j++){
                if(T[j]<=k) t2=t2+T[j];
                else t2=t2+k;
            }

        output<<"case #"<<i<<": "<<t1<<" "<<t2<<endl;
    }



    return 0;
}

