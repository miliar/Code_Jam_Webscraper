# include <iostream>
using namespace std;
bool verifica(int *numbers){
    for(int i = 0; i < 10; i++){
        if(numbers[i] == 0)
            return false;

    }
    return true;
}

int main(){
    int numbers[10], t, n;
    bool complete = false;

    cin >> t;
    int j = 0;
    while(j < t){//Caso de teste
        j++;
        //cout << "CASO " << j << endl;
        cin >> n;
        int x, q = 1, N;
        complete = false;

        for(int i = 0; i < 10; i++)
            numbers[i] = 0;

        while(complete == false){
            //cout << "CASO " << j << endl;
            if(n == 0){
                cout << "Case " << j << ": Insomnia" << endl;
                break;
            }

            N = q*n;
            q++;
            int backup;
            backup = N;
            do{
                //cout << N << endl;
                x = N % 10;
                numbers[x] += 1;
                complete = verifica(numbers);
                if(complete == true){
                    cout <<"Case #" << j << ": "<< backup << endl;
                    break;
                }
                if(N < 10)
                    break;
                N = N / 10;
            }while(true);
            if(complete)
                break;
        }
    }

    return 0;
}
