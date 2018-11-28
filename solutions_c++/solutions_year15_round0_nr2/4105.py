#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>
#include<cmath>


using namespace std;
int func(vector <int> a,int max,int def);

int min(int x,int y){
    if(x>y)
        return y;
    return x;
}
int min1(int w,int x,int y){
    int m=w;
    if(x<m)
        m=x;
    if(y<m)
        m=y;
    return m;
}

main(){
    ifstream in("B-small-attempt5.in");
    ofstream out("output.txt");
    int test;
    in>>test;
    for(int t=1;t<=test;t++){
        vector<int> v1;
        int No,te,max=0;
        in>>No;
        for(int i=0;i<No;i++){
            in>>te;
            if(max<te)
                max=te;
            v1.push_back(te);
        }
        out<<"Case #"<<t<<": "<<min(max,func(v1,max,0))<<endl;
    }

}
int div(vector<int>&a,int &max,int def){
    int c=0;
    if(def==0)
        return 0;
    if(def>=max){
        max=1;
        return 0;
    }
    for(int i=0;i<a.size();i++){
        if(a[i]==max){
            a.push_back(def);
            a.push_back(a[i]-def);
            a.erase(a.begin()+i);
            i--;
            c++;
        }
    }
    return c;
}

int func(vector <int> a,int max,int def){
    if(max<=1)
        return 1;
    int c=div(a,max,def);
    int max1=0;
    for(int i=0;i<a.size();i++)
        if(a[i]>max1)
            max1=a[i];
    if(max!=1)
        return min(c+max1,c+min1(func(a,max1,2),func(a,max1,3),func(a,max1,4)));
    else
        return c+max1;
}
