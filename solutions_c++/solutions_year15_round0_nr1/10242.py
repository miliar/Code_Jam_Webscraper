    #include <iostream>
    using namespace std;
     
    int main() {
    int t;
    cin>>t;
    for(int q=1;q<=t;q++){
    int sm=0,f=0,sd=0,ad=0;
    cin>>sm;
    char a[sm+1];
    cin>>a;
    int i=0;
    for(i=0;i<sm+1;i++){
   
    if(ad<i){f++;ad++;}
  
    ad+=a[i]-'0';
   
    }
    cout<<"case #"<<q<<": "<<f<<endl;
    
    };
    return 0;
    }