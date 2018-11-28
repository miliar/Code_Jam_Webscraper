#include <iostream>
#include <cstdio>

using namespace std;

int lastNum(int num);
int main()
{
    freopen("A-small-attempt0.in" , "r" , stdin);
    freopen("myOut.txt" , "w" , stdout);
    int T;
    scanf("%d" , &T);
    for(int counter = 1; counter <= T; counter ++){
        int num;
        scanf("%d" , &num);
        if(num != 0){
            int res = lastNum(num);
            printf("Case #%d: %d\n" , counter , res);
        }
        else{
            printf("Case #%d: INSOMNIA\n" , counter);
        }
    }
    return 0;
}

int lastNum(int num){
    bool visited[10];
    for(int counter = 0; counter < 10; counter ++){
        visited[counter] = false;
    }
    int unvisited = 10;
    int cnum;
    int mul = 1;
    while(unvisited > 0){
        cnum = num * mul;
        while(cnum > 0){
            if(!visited[cnum % 10]){
                visited[cnum % 10] = true;
                unvisited --;
            }
            cnum /= 10;
        }
        mul ++;
    }
    return num * (mul - 1);
}
