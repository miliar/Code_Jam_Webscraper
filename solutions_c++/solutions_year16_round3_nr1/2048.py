#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

bool breakCondition(pair<int,char> p[26],int n){
    int c = 0;
    for(int i = 0;i < n;i++){
        if(p[i].first == 1)
            c++;
        else if(p[i].first != 0)
            return false;
        if(c > 2)
            return false;
    }
    return true;
}
bool removable(pair<int,char> p[26],int n,int index){
    double THRESHOLD = 0.5;
    p[index].first--;
    int sum = 0;
    for(int i = 0;i < n;i++)
        sum += p[i].first;
    for(int i = 0;i < n;i++){
        double avg = p[i].first/(1.0*sum);
        if(avg > THRESHOLD){
            p[index].first++;
            return false;
        }
    }
    return true;
}
void evaluate(int *a,int n){
    pair<int,char> p[26];
    for(int i = 0;i < n;i++)
        p[i] = make_pair(a[i],'A' + i);
    sort(p,p+n,greater<pair <int,char> >());
    while(!breakCondition(p,n)){
        p[0].first--;
        cout << p[0].second;
        for(int i = 0;i < n;i++){
            if(p[i].first != 0 && removable(p,n,i)){
                cout << p[i].second;
                break;
            }
        }
        cout << " ";
        sort(p,p+n,greater<pair <int,char> >());
    }
    for(int i = 0;i < n;i++){
        if(p[i].first == 1){
            cout << p[i].second;
            p[i].first--;
        }
    }
}
int main()
{
    int t;
    cin >> t;
    for(int cases = 1;cases <= t;cases++){
        int n;
        cin >> n;
        int p[26];
        memset(p,0,sizeof(p));
        for(int i = 0;i < n;i++)
            cin >> p[i];
        cout << "Case #" << cases << ": ";
        evaluate(p,n);
        cout << endl;
    }
    return 0;
}
