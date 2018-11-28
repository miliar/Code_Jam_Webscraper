#include <iostream>
#include <cstdio>

using namespace std;

void removeCharFromString( string &str, char charToRemove ) {
   std::size_t found = str.find_first_of(charToRemove);
   str.erase(found , 1);
}

void prnum(int num , int tries){
    for(int c = 0; c < tries; c++){
        printf("%d" , num);
    }
}

int main()
{
    freopen("A-large (2).in" , "r" , stdin);
    freopen("out.txt" , "w" , stdout);
    int t;
    std::string str;
    scanf("%d" , &t);
    for(int c = 1; c <= t; c++){
        int nums[10];
        for(int c1 = 0; c1 < 10; c1++){
            nums[c1] = 0;
        }
        cin >> str;
        while(str.find('Z') != std::string::npos){
            removeCharFromString(str , 'Z');
            removeCharFromString(str , 'E');
            removeCharFromString(str , 'R');
            removeCharFromString(str , 'O');
            nums[0] ++;
        }
        while(str.find('W') != std::string::npos){
            removeCharFromString(str , 'T');
            removeCharFromString(str , 'W');
            removeCharFromString(str , 'O');
            nums[2] ++;
        }
        while(str.find('X') != std::string::npos){
            removeCharFromString(str , 'S');
            removeCharFromString(str , 'I');
            removeCharFromString(str , 'X');
            nums[6] ++;
        }
        while(str.find('U') != std::string::npos){
            removeCharFromString(str , 'F');
            removeCharFromString(str , 'O');
            removeCharFromString(str , 'R');
            removeCharFromString(str , 'U');
            nums[4] ++;
        }
        while(str.find('O') != std::string::npos){
            removeCharFromString(str , 'N');
            removeCharFromString(str , 'E');
            removeCharFromString(str , 'O');
            nums[1] ++;
        }
        while(str.find('R') != std::string::npos){
            removeCharFromString(str , 'T');
            removeCharFromString(str , 'H');
            removeCharFromString(str , 'E');
            removeCharFromString(str , 'R');
            removeCharFromString(str , 'E');
            nums[3] ++;
        }
        while(str.find('F') != std::string::npos){
            removeCharFromString(str , 'F');
            removeCharFromString(str , 'I');
            removeCharFromString(str , 'V');
            removeCharFromString(str , 'E');
            nums[5] ++;
        }
        while(str.find('S') != std::string::npos){
            removeCharFromString(str , 'S');
            removeCharFromString(str , 'E');
            removeCharFromString(str , 'V');
            removeCharFromString(str , 'E');
            removeCharFromString(str , 'N');
            nums[7] ++;
        }
        while(str.find('G') != std::string::npos){
            removeCharFromString(str , 'I');
            removeCharFromString(str , 'E');
            removeCharFromString(str , 'G');
            removeCharFromString(str , 'H');
            removeCharFromString(str , 'T');
            nums[8] ++;
        }
        while(str.find('N') != std::string::npos){
            removeCharFromString(str , 'N');
            removeCharFromString(str , 'I');
            removeCharFromString(str , 'N');
            removeCharFromString(str , 'E');
            nums[9] ++;
        }
        printf("Case #%d: " , c);
        for(int c2 = 0; c2 < 10; c2 ++){
            prnum(c2 , nums[c2]);
        }
        printf("\n");
    }
    return 0;
}
