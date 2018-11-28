#include <iostream>

using namespace std;
int v[17];
void f(int a){
    for(int i=1;i<5;i++){
        for(int j=1;j<5;j++){
            int x;
            cin>>x;
            if(i==a)
            v[x]++;
        }
    }
}
int main()
{
    int t;
    cin>>t;
    int c=1;
    while(t--){

        for(int i=0;i<17;i++){
            v[i]=0;
        }
        int a ,b;
        cin>>a;
        //cout << "foo" << endl;
        f(a);
        //cout << "foo" << endl;
        cin>>b;

        f(b);
        int r=0;
        string resp="Volunteer cheated!";
        for(int i=1;i<17;i++){
            if(v[i]>1 and r==0){
                r=i;
            }
            else{
                if(r>0 and v[i]>1)
                resp="Bad magician!";
            }

        }
        if(r>0 and resp.compare("Volunteer cheated!")==0)
        cout<<"Case #"<<c<<": "<<r<<endl;
        else
        cout<<"Case #"<<c<<": "<<resp<<endl;
        c++;
    }
    return 0;
}
