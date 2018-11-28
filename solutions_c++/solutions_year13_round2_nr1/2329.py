#include <iostream>
#include <iomanip>
#include <cstdio>
#include <queue>
#include <vector>
#include <list>
#include <algorithm>
#include <cstdlib>
#include <string>
#include <cstring>
using namespace std;

#define all(x) (x).begin(),(x).end()
#define min(x,y) ((x)<(y)?(x):(y))
#define max(x,y) ((x)>(y)?(x):(y))

int cas;
int a;
int n;
int s[111];

int comp(const void *elem1, const void *elem2)
{
    return *((int*)(elem1))-*((int*)(elem2));
}

int main(){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int temp;
    int t_count;
    int all_count;

    cin>>cas;

    for (int l=1; l<=cas; l++){
        cin>>a>>n;
        for (int i=0; i<n; i++)
            cin>>s[i];
        //if a == 1
        printf("Case #%d: ", l);
        if (a == 1) {cout<<n<<endl;continue;}
        qsort(s, n, sizeof(int), comp);
        all_count = 0;
        for (int i=0; i<n; i++){
            if (s[i]<a)
                a+=s[i];
            else{
                temp = a;
                t_count = 0;
                while (s[i]>=temp){
                    temp += temp-1;
                    t_count++;
                }
                if (t_count>=n-i){
                    all_count+=n-i;
                    break;
                }else{
                    a = temp+s[i];
                    all_count += t_count;
                }
            }
        }
        cout<<all_count<<endl;
    }
	return 0;
}