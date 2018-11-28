#include <cstdio>
#include <iostream>
#include <map>

using namespace std;

map<int,int> square;

// For the small problem set

#define HIGHEST 1000
#define LOWEST 1

void make_square(){

    int i = LOWEST;

    while(i * i <= HIGHEST){

        square[i * i] = i;

        i++;
    }

}

bool check_palindrome(int num){

    int n = num, dig;
    int rev = 0;
    while (num > 0)
    {
         dig = num % 10;
         rev = rev * 10 + dig;
         num = num / 10;
    }

    if (n == rev){
        //printf("%d \n",rev);
        return true;
    }
    return false;
}

int check_square(int num){

    map<int,int>::iterator i = square.find(num);

    if (i == square.end())
        return 0;
    else return square[num];
}


int main(){

    int cases;
    int low,high,result;

    scanf("%d",&cases);

    for(int index = 0 ; index < cases ; index++){

        scanf("%d %d",&low,&high);

        //printf("%d %d\n",low,high);

        bool pass;
        int sqr_root;

        result = 0;

        make_square();

        for(int num = low; num <= high; num++){
            pass = false, sqr_root = 0;

        // 1. Is the number palindrome

            pass = check_palindrome(num);

            if(!pass) continue;

        // 2. Is it Square, if so find the square root of it
            sqr_root = check_square(num);

            if(!sqr_root) continue;

            //printf("Real: %d, Root: %d\n",num,sqr_root);

        // 3. Is the square root also a palindrome

            pass = check_palindrome(sqr_root);

            if(!pass) continue;

         // If all tests are passed, we increase the result by one
            result++;
        }

        printf("Case #%d: %d\n",index+1,result);
    }

    return 0;
}
