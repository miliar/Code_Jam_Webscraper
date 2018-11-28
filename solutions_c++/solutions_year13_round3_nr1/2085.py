#include<iostream>
#include<string>

using namespace std;

bool isConstant(char a);
bool countConstant(string a,int b);
bool countConstant_helper(string a,int b);
int find_n_value(string a,int b);

int main(){
    int t;
    cin>>t;
    int n_length[t],n_value[t];
    string name[t];
    for(int i=0;i<t;i++){
        cin>>name[i];
        cin>>n_length[i];
    }
    for(int i=0;i<t;i++){
        n_value[i]=find_n_value(name[i],n_length[i]);
    }
    for(int i=0;i<t;i++){
        cout<<"Case #"<<i+1<<": "<<n_value[i]<<endl;
    }
}

bool isConstant(char a){
    if(a=='a'||a=='e'||a=='i'||a=='o'||a=='u'){
        return 0;
    }
    return 1;
}

bool countConstant_helper(string a,int b){
    bool c=1;
    for(int i=0;i<b;i++){
        c=c&&isConstant(a[i]);
    }
    return c;
}

bool countConstant(string a,int b){
    int len=a.length();
    string d;
    for(int i=0;i<=len-b;i++){
        d=a.substr(i,b);
        if(countConstant_helper(d,b)){
            return 1;
        }
    }
    return 0;
}

int find_n_value(string a,int b){
    int len=a.length();
    int count=0;
    for(int i=b;i<=len;i++){
        for(int j=0;j<len-i+1;j++){
                if(countConstant(a.substr(j,i),b)){
                    count++;
                }
        }
    }
    return count;
}
