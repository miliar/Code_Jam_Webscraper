#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>
#include<cmath>


using namespace std;
int docalc(vector <int> a,int max,int def);

int min(int x,int y);
int minimu1(int w,int x,int y){
    int m=w;
    if(x<m)
        m=x;
    if(y<m)
        m=y;
    return m;
}

main(){
    ifstream in("B-small-attempt1.in");
    ofstream out("output.txt");
    int T;
    in>>T;
    for(int t=1;t<=T;t++){
        vector<int> v1;
        int No,y1,max=0;
        in>>No;
		int i=0;
        while(i<No){
            in>>y1;
            if(max<y1)
                max=y1;
            v1.push_back(y1);
			i++;
        }
        out<<"Case #"<<t<<": "<<min(max,docalc(v1,max,0))<<endl;
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

int docalc(vector <int> a,int max,int def){
    if(max<=1)
        return 1;
    int c=div(a,max,def);
    int max1=0;
    for(int i=0;i<a.size();i++)
        if(a[i]>max1)
            max1=a[i];
    if(max!=1)
        return min(c+max1,c+minimu1(docalc(a,max1,2),docalc(a,max1,3),docalc(a,max1,4)));
    else
        return c+max1;
}
int min(int x,int y){
    if(x>y)
        return y;
    return x;
}
