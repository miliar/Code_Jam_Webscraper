#include <iostream>

bool seen[10];

bool addDigits(int num);

int main(int argc, char* argv[]){
    int t =0;
    std::cin >> t;
    int caseVal = 1;
    while(t--){
        for(int i = 0; i < 10; i++) seen[i] = false;
        int N = 0;
        std::cin >> N;

        if(N != 0){
            int i = 1;
            bool done = false;
            int num = N;
            while(!done){
                num = N*i;
                i++;
                done = addDigits(num);
            }

            std::cout << "Case #" << caseVal << ": " << num << std::endl;
        } else {
            std::cout << "Case #" << caseVal << ": " << "INSOMNIA" << std::endl;

        }
        caseVal++;
    
    }


}

bool addDigits(int num){
    const int ten = 10;
    bool retVal = true;

    while(num/ten != 0){
        int dig = num%ten;
        seen[dig] = true;
        num = num/ten;
    }
    seen[num] = true;

    for(int  i = 0; i < ten; i++){
        if(seen[i] == false){
            retVal = false;
            break;
        }
    }

    return retVal;

}
