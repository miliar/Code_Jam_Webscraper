#include <bits/stdc++.h>

using namespace std;

int main(){
    ifstream cin("A-large.in");
    ofstream cout("salidaT.txt");
    int n;
    unsigned long long int num, resp,resp2;
    cin>>n;
    int c = 0;
    while (n--){
        int voy = 1;
        cin>>num;
        if (num == 0){
            cout<<"Case #"<<++c<<": INSOMNIA"<<endl;
            continue;
        }
        int van = 0;
        int es = 0;
        int arr[10]={0};
        while (true){
            resp = voy * num;
            resp2 = resp;
            while (resp>0){
                int d = resp%10;
                resp /= 10;
                if (!arr[d]){
                    van++;
                    arr[d]=true;
                }

                //cin>>es;
            }
            if (van==10){
                es = resp;
                break;
            }
            voy++;
        }
        cout<<"Case #"<<++c<<": "<<resp2<<endl;
    }

    return 0;
}
