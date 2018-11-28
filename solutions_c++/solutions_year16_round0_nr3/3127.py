#include <iostream>
#include <vector>
#include <math.h>
#include <cmath>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

void reverse(char str[], int length)
{
    int start = 0;
    int end = length -1;
    while (start < end)
    {
        swap(*(str+start), *(str+end));
        start++;
        end--;
    }
}

char* itoa(long long num, char* str, int base)
{
    int i = 0;
    /* Handle 0 explicitely, otherwise empty string is printed for 0 */
    if (num == 0)
    {
        str[i++] = '0';
        str[i] = '\0';
        return str;
    }
    // Process individual digits
    while (num != 0)
    {
        int rem = num % base;
        str[i++] = (rem > 9)? (rem-10) + 'a' : rem + '0';
        num = num/base;
    }
    str[i] = '\0'; // Append string terminator
    // Reverse the string
    reverse(str, i);
    return str;
}

int main(){
    vector<string> store;
    int tc,n,j,mul;
    bool foundPrime;
    scanf("%d",&tc);
    for(int tci=1;tci<=tc;tci++){
        scanf("%d %d",&n,&j);
        mul=0;
        printf("Case #%d:\n",tci);
        while(j>0){
            long long cur = (1<<(n-1))+1+2*mul++;
            char bin[1000];
            itoa(cur,bin,2);
            string toStore = bin;
            string toAppend = "";
            foundPrime = false;
            for(int i=2;i<11;i++){
                if(i>2){
                    cur = stoll(bin,nullptr,i);
                }
                int k;
                for(k=2;k<101;k++){
                    if(!(cur%k)) {toAppend += " "+to_string(cur/k); break;}
                }
                if(k == 101) {foundPrime = true;break;}
            }
            if(foundPrime) continue;
            toStore += toAppend;
            store.push_back(toStore);
            j--;
        }
        for(int i=0;i<store.size();i++){
            printf("%s\n",store[i].c_str());
        }
    }
    return 0;
}