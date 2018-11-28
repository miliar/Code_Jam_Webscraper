#include <bits/stdc++.h>

using namespace std;

const int MAXN = 1010;
double naomi[MAXN];
double ken[MAXN];
bool used[MAXN];
int n;

int war(){
    int c = 0 , pn = 0 , pk  = 0;
    for(int i = 0 ; i < n ; i++){
        if(naomi[pn] < ken[pk]){
            pn++;pk++;
        } else {
            pk++;c++;
        }
    }
    return c;
}

int dwar(){
    int c = 0 , pn = 0 , pk  = 0;
    for(int i = 0 ; i < n ; i++){
        if(naomi[pn] < ken[pk]){
            pn++;
        } else {
            pn++;pk++;c++;
        }
    }
    return c;
}

int main(){
    //freopen("in.txt","r",stdin);
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    int casos;
    cin >> casos;
    for(int caso = 1 ; caso <= casos ; caso++){
        cin >> n;
        for(int i =  0 ; i < n ; i++){
            cin >> naomi[i];
        }
        for(int i =  0 ; i < n ; i++){
            cin >> ken[i];
        }
        sort(naomi,naomi+n);
        sort(ken,ken+n);
        cout << "Case #" << caso << ": " << dwar() << " " << war() << endl;
    }
    return 0;
}
