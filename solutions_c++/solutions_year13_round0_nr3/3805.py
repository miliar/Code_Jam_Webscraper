#include <stdio.h>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

int x;
vector<unsigned long long> list;
int ct;

int t;
FILE* file;

bool palindrome(unsigned long long l){
    ostringstream convert;
    convert << l;
    string str = convert.str();
    return str.compare(string(str.rbegin(),str.rend()))==0;
}

int main(){
    for(int i=1;i<10000100;i++){
        unsigned long long test = i*i;
        if(palindrome(i) && palindrome(test)){
            list.push_back(test);
            ct++;
        }
    }
    printf("OK %d\n",ct);
    scanf("%d",&t);
    file = fopen("fairandsquaresmall.out", "w");
    for(int i=0;i<t;i++){
        unsigned long long a,b;
        scanf("%llu%llu",&a,&b);
        //printf("%d\n",upper_bound(list.begin(),list.end(),b)-lower_bound(list.begin(),list.end(),a));
        fprintf(file,"Case #%d: ",i+1);
        fprintf(file,"%d\n",upper_bound(list.begin(),list.end(),b)-lower_bound(list.begin(),list.end(),a));
    }
}

