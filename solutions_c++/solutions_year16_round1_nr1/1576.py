//
// Created by 강경완 on 16. 4. 16..
//


#include <iostream>
#include <list>

using namespace std;

int n;
char ary[111][1111];
int main(){


    cin >> n;

    for(int i=0; i<n; i++){
        cin >> ary[i];
    }

    for(int i=0; i<n; i++){
        list<char> l;
        l.push_front(ary[i][0]);
        int temp;
        for(int j=1; j<strlen(ary[i]); j++){
            temp = l.front();
            if(temp <= ary[i][j]){
                l.push_front(ary[i][j]);
            }else{
                l.push_back(ary[i][j]);
            }

        }
        printf("Case #%d: ", i+1);
        for(list<char>::iterator itor=l.begin(); itor != l.end(); itor++){
            printf("%c", *itor);
        }
        cout << endl;

    }



}