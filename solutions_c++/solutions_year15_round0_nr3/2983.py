#include <bits/stdc++.h>
using namespace std;

bool sinal, sinalPart;

char mult(char a, char b, bool isLoopProd){
    char answer;

    if (sinal){
        switch (a){
        case 'i':
            switch (b){
            case 'i':
                answer = '1';
                sinal = false;

                break;
            case 'j':
                answer = 'k';
                sinal = true;

                break;
            case 'k':
                answer = 'j';
                sinal = false;

                break;
            case '1':
                answer = 'i';
                sinal = true;

                break;
            }
            break;

        case 'j':
            switch (b){
            case 'i':
                answer = 'k';
                sinal = false;

                break;
            case 'j':
                answer = '1';
                sinal = false;

                break;
            case 'k':
                answer = 'i';
                sinal = true;

                break;
            case '1':
                answer = 'j';
                sinal = true;

                break;
            }

            break;
        case 'k':
            switch (b){
            case 'i':
                answer = 'j';
                sinal = true;

                break;
            case 'j':
                answer = 'i';
                sinal = false;

                break;
            case 'k':
                answer = '1';
                sinal = false;

                break;
            case '1':
                answer = 'k';
                sinal = true;

                break;
            }
            break;
        case '1':
            answer = b;
            sinal = true;

            break;

        }

    }
    else{
        switch (a){
        case 'i':
            switch (b){
            case 'i':
                answer = '1';
                sinal = true;

                break;
            case 'j':
                answer = 'k';
                sinal = false;

                break;
            case 'k':
                answer = 'j';
                sinal = true;

                break;
            case '1':
                answer = 'i';
                sinal = false;

                break;
            }
            break;

        case 'j':
            switch (b){
            case 'i':
                answer = 'k';
                sinal = true;

                break;
            case 'j':
                answer = '1';
                sinal = true;

                break;
            case 'k':
                answer = 'i';
                sinal = false;

                break;
            case '1':
                answer = 'j';
                sinal = false;

                break;
            }

            break;
        case 'k':
            switch (b){
            case 'i':
                answer = 'j';
                sinal = false;

                break;
            case 'j':
                answer = 'i';
                sinal = true;

                break;
            case 'k':
                answer = '1';
                sinal = true;

                break;
            case '1':
                answer = 'k';
                sinal = false;

                break;
            }
            break;
        case '1':
            answer = b;
            sinal = false;

            break;

        }
    }
    if (isLoopProd && !sinalPart)
        sinal = !sinal;
    return answer;
}
int main (){

    int  N, D, T;
    string s;
    bool running, possible, particular;
    char C, prod, part;
    cin >> N;

    for (int a = 0; a < N; a++){
        cin >> D;
        cin >> T;
        cin >> s;

        sinal = running = true;
        possible = particular = false;


        C = 'i';
        prod = '1';

        for (int b = 0; b < s.size(); b++)
            prod = mult(prod,s[b], false);
        char loopProd = prod;
        sinalPart = sinal;
        prod = '1';
        sinal = running = true;

        for (int t=0; t < T; t++){

            if (possible){

                int left = (T-t)%4;;

                switch(left){
                case 0:
                    break;
                case 1:
                    prod = mult(prod, loopProd, true);
                    break;
                case 2:
                    prod = mult(prod, loopProd, true);
                    prod = mult(prod, loopProd, true);
                    break;
                case 3:
                    prod = mult(prod, loopProd, true);
                    prod = mult(prod, loopProd, true);
                    prod = mult(prod, loopProd, true);
                    break;
                }

                //cout << "\nleft = " << left << "\nProd Final = "<< prod << "\nSinal = " << sinal << "\nLoopProd = " << loopProd << "\nLoopSinal = " << sinalPart;
                break;
            }else{
                for (int b=0; b < s.size();b++){

                    prod = mult(prod, s[b], false);
                  /*  if (!sinal)
                        cout << "-";
                    cout << prod << endl;*/
                    if (prod==C){
                        prod = '1';
                        if (C=='i')
                            C = 'j';
                        else if (C=='j')
                            C = 'k';
                        else if (C=='k'){
                            possible = true;
                            C = 'a';
                        }
                    }

                }

            }


        }


        string Answer;
        if (possible && prod == '1' && sinal == true)
            Answer = "YES";
        else
            Answer = "NO";
        cout << "Case #" << (a + 1) << ": " << Answer <<  '\n';
    }
    return 0;
}

