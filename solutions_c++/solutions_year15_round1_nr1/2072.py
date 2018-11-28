#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>


using namespace std;
ifstream fin("largea.in.txt");
ofstream fout("largea.out");
int main()
{
    int t;
    fin>>t;
    for(int h=0;h<t;h++){
        int n;
        fin>>n;
        vector <int> ary(n);
        for(int i=0;i<n;i++)
            fin>>ary[i];
        int way1=0;
        int ma=0;
        int way2=0;
        for(int i=0;i<n-1;i++){
            if(ary[i+1]<ary[i]){
                way1+=ary[i]-ary[i+1];
                if(ary[i]-ary[i+1]>ma)
                    ma=ary[i]-ary[i+1];
            }
        }
        int carry=0;
        for(int i=0;i<n-1;i++){

            int temp=ary[i]-ma;
            if(temp<0){
                way2+=ary[i];
                ary[i]=0;
            }
            else{
                ary[i]-=ma;
                way2+=ma;
            }
        }
        fout<<"Case #"<<h+1<<": "<<way1<<" "<<way2<<endl;
    }
}
