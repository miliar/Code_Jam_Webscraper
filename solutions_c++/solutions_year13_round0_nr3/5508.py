#include<iostream>


/*
basic palindrome
1       1       ok
2       4       ok
3       9       ok
4       16      No as 16 is not a pal.
*/

bool isPal(int i){
        if(i == 1) return true;
        char word[100] = {0};
        int len = 0;
        int nopal = 0;
        snprintf(word,100,"%d",i);
        len = strlen(word);
        if(len == 1) return true;
        if(len == 2){if(word[0] == word[1]){return true;} else {return false;}}
        int counter = len/2;
        for(int j=0, k=len-1;j<counter;j++,k--){
                if(word[j] != word[k]){
                        return false;
                }
        }
        return true;
}

int isSquar(int i){
        if(i == 1) return true;
        int len = i/2;
        for(int j=1;j<=len;j++){
                if(j*j == i){
                        return j;
                }
        }
        return -1;
}

int getNumbers(int A, int B){
        int palcount = 0;
        int first = -1, second = -1, sqr = -1;
        first = (A > B)?B:A;
        second = (A > B)?A:B;
        for(int i =first;i<=second;i++){
                if(isPal(i) == true){
                        if((sqr = isSquar(i)) != -1){
                                if(isPal(sqr) == true) {
                                        //std::cout<<"psqr + pal : "<<i<<std::endl;
                                        palcount++;
                                }
                        }
                }
        }
        return palcount;
}

int main(int argc, char **argv){
        int T=0, val = -1;
        std::cin>>T;
        //char A[100] = {0};
        //char B[100] = {0};
        int A = -1;
        int B = -1;

        for(int i=0;i<T;i++) {
                std::cin>>A>>B;
                //std::cout<<"INPUT : "<<A<<"   "<<B<<std::endl;
                val = getNumbers(A,B);
                std::cout<<"Case #"<<i+1<<": "<<val<<std::endl;
        }
}
