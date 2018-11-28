#include <bits/stdc++.h>
using namespace std;

int main()
{
 //  freopen("in.txt","r",stdin);
   // freopen("out.txt","w",stdout);
    int t,count,k,minimum,n,i,p,q,u;
    int a[10];
    vector<int>vec;
    cin >> t;
    for (u = 1; u <= t;u++){
        cin >> n;
        for (i = 0; i < n; i++){
            cin >> a[i];
        }
        if(n == 1){
            if(a[0] == 1){
                cout <<"Case #"<<u<<": "<<"1"<<endl;
                continue;
            }
            if(a[0] == 2){
                cout <<"Case #"<<u<<": "<<"2"<<endl;
                continue;
            }
            if(a[0] == 3){
                cout <<"Case #"<<u<<": "<<"3"<<endl;
                continue;
            }
            if(a[0] == 4){
                cout <<"Case #"<<u<<": "<<"3"<<endl;
                continue;
            }
            if(a[0] == 5){
                cout <<"Case #"<<u<<": "<<"4"<<endl;
                continue;
            }
            if(a[0] == 6){
                cout <<"Case #"<<u<<": "<<"4"<<endl;
                continue;
            }
            if(a[0] == 7){
                cout <<"Case #"<<u<<": "<<"5"<<endl;
                continue;
            }
            if(a[0] == 8){
                cout <<"Case #"<<u<<": "<<"5"<<endl;
                continue;
            }
            if(a[0] == 9){
                cout <<"Case #"<<u<<": "<<"5"<<endl;
                continue;
            }
        }
        for (i = 0; i < n; i++){
            vec.push_back(a[i]);
        }
        k = vec.size();
        sort(vec.begin(),vec.end());
        count = 0;
        minimum = 1000000;
        int m = 3;
        p = 0;
        while(p!=1){
            p = vec[k-1];
            q = vec[k-2];
            int tmp;
            tmp = __gcd(p,q);

            if(tmp != 1 && tmp != p){
                vec.pop_back();
                vec.push_back(tmp);
                vec.push_back(p-tmp);
                sort(vec.begin(),vec.end());
            }
            else {
                vec.pop_back();
                vec.push_back(p/2);
                vec.push_back(p - (p/2));
                sort(vec.begin(),vec.end());
            }
            if(count+p < minimum){
                minimum = count+p;
            }
           /* for (i = 0; i < vec.size(); i++){
                    cout << vec[i];
                }
                cout << " ";
                cout << minimum<<endl;*/
           k = vec.size();
            count++;
        }
         vec.clear();
        cout <<"Case #"<<u<<": "<<minimum<<endl;
    }
}
