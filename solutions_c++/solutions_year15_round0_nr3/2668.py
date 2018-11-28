#include <iostream>
#include <list>
using namespace std;


char judgeChar(int ci, int cj, int ck){
    if(ci %2== cj%2 && cj %2  != ck %2)
        return 'k';
    if(ci %2 == ck %2 && cj %2  != ck %2)
        return 'j';
    if(ci %2 != ck %2 && cj %2  == ck %2)
        return 'i';
    if(ci %2 == ck %2 && cj %2  == ck %2)
        return '1';
    return 0;
}

int judgePosNeg( char vote, char judgedChar, int last_symbol, int reverse){
    switch(judgedChar){
        case 'i':
            {
                if( (reverse == 0 && vote == 'j') || (reverse == 1 && vote== 'k'))
                {
                    return last_symbol*(-1); 
                }
                else return last_symbol;
            }    
        case 'j':
            {
                if( (reverse == 0 && vote == 'k' )|| (reverse == 1 && vote== 'i'))
                {
                    return last_symbol*(-1); 
                }
                else return last_symbol;

            }
        case 'k':{
                 if( (reverse == 0 && vote == 'i') || (reverse == 1 && vote== 'j'))
                {
                    return last_symbol*(-1); 
                }
                else return last_symbol;

        }
        case '1':{
            return last_symbol*(-1);
        }
        default:
            return 0;

    }
}
int worker( int L, int K, char* unit){
    if(L==1) return 0;
    if(L<3 && L*K <3) return 0;
    int* counti_small = new int[L];
    int* countj_small = new int[L];
        int* countk_small = new int[L];
        for(int i = 0; i< L; i++){
            counti_small[i] = 0;
                        countj_small[i] = 0;

            countk_small[i] = 0;

        }
    for(int i=0; i< L; i++){
        switch(unit[i]){
            case 'i':
                {
                    if(i == 0) counti_small[i]++;
                    else
                    {counti_small[i] = counti_small[i-1]+1;
                    countj_small[i] = countj_small[i-1];
                    countk_small[i] = countk_small[i-1];
                    }
                    break;
                    // int last_value=0;
                    // for(int j = 0; j< X; j++){
                    //     int pointer = j*L/8;
                    //     value = (last_value + 1)%4;
                    //     counti[pointer] |= value<<15-(j*L)%8*2);
                    //     last_value = value;
                    // }
                }
            case 'j':
            {
                if(i == 0) countj_small[i]++;
                    else{
                    countj_small[i] = countj_small[i-1]+1;
                    counti_small[i] = counti_small[i-1];
                    countk_small[i] = countk_small[i-1];
                }
                break;

            }
            case 'k':{
                 if(i == 0) countk_small[i]++;
                    else{
                    countk_small[i] = countk_small[i-1]+1;
                    countj_small[i] = countj_small[i-1];
                    counti_small[i] = counti_small[i-1];
                }
                break;
            }
        }

    }
    int find_flag = 0;
    int last_symbol = 1;
    int seperator1= 0;
    int seperator1_symbol = 0;
    int seperator2_symbol = 0;
    int seperator2 = L*K;
    for(int i = 0; i< L*K; i++){
        //find i
        int counti = (counti_small[L-1]*(i/L)+counti_small[ i%L ])%4;
        int countj = (countj_small[L-1]*(i/L)+countj_small[ i%L ])%4;
        int countk = (countk_small[L-1]*(i/L)+countk_small[ i%L ])%4;
        char judgedChar = judgeChar(counti, countj, countk);
        int symbol = judgePosNeg(unit[i%L], judgedChar, last_symbol, 0);
        last_symbol = symbol;
        if(find_flag == 0){
            if( judgedChar != 'i') continue;
            else {
                 find_flag =1 ;
                seperator1 = i;
            }
        }
    }
    if(last_symbol != -1 || find_flag == 0) return 0;
    if(seperator1 >L*K-2) return 0;

    for (int i = L*K-1; i> seperator1; i--){
        int counti = ( counti_small[L-1]*K - (counti_small[L-1]*((i-1)/L)+counti_small[ (i-1)%L ]))%4;
        int countj = ( countj_small[L-1]*K - (countj_small[L-1]*((i-1)/L)+countj_small[ (i-1)%L ]))%4;
        int countk = ( countk_small[L-1]*K - (countk_small[L-1]*((i-1)/L)+countk_small[ (i-1)%L ]))%4;
        char judgedChar = judgeChar(counti, countj, countk);
        seperator2 = i;
        if( judgedChar != 'k') continue;
        else break;
    }
    if(seperator2 <= seperator1+1) return 0;
    if(seperator1 >L*K-2) return 0;

    int counti = ( (counti_small[L-1]*((seperator2-1)/L)+counti_small[ (seperator2-1)%L ]) - (counti_small[L-1]*(seperator1/L)+counti_small[ seperator1%L ])  )%4;
    int countj = ( (countj_small[L-1]*((seperator2-1)/L)+countj_small[ (seperator2-1)%L ]) - (countj_small[L-1]*(seperator1/L)+countj_small[ seperator1%L ])  )%4;
    int countk = ( (countk_small[L-1]*((seperator2-1)/L)+countk_small[ (seperator2-1)%L ]) - (countk_small[L-1]*(seperator1/L)+countk_small[ seperator1%L ])  )%4;
    char judgedChar = judgeChar(counti, countj, countk);
    if(judgedChar !='j')
        return 0;

    return 1;

}


int main(){
    int testCase;
    cin>>testCase;
    
    for(int i = 0; i< testCase ; i++){
        int L, X;
        cin>>L>>X;
        char * unit = new char[L];
        cin>> unit;
        if(worker(L,X, unit) == 1)

             cout<<"Case #"<<i+1<<": "<<"YES"<<endl;
         else 
            cout<<"Case #"<<i+1<<": "<<"NO"<<endl;
    }

}