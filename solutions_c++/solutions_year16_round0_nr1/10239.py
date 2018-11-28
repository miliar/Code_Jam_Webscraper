#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;
bool func (int arr[]);

int main()
{
    int const myArray[] = {1,10,100,1000,10000,100000,1000000,10000000};
    int seen[10];
    int d = 0, temp = 0;
    bool isSeen , allSeen;
    int multiplier;
    ofstream myFile;
    myFile.open("A-large.out");
    long int testCases = 0;
    long int num = 0;
    ifstream input ("A-large.in");
    input >> testCases;

    for (int i = 0 ; i < testCases; i++){
        input >> temp;
        multiplier = 2;
        num = temp;
        for(int i = 0; i<10;i++){
        seen[i] = 0;
        }
        if (num == 0){
            myFile << "Case #" << i+1 << ": INSOMNIA" << endl;
        }
        else{
            allSeen = false;
            isSeen = false;
            while(allSeen == false){
                if (num > 0 and num <=9){
                    seen[num] = 1;
                    isSeen = func(seen);
                    if (isSeen == true){
                        myFile << "Case #" << i+1 << ": " << num << endl;
                        allSeen = true;
                    }
                }
                else if (num >=10 and num <=99){

                        for (int i = 1; i >=0; i--)
                        {
                            d = num/myArray[i];
                            d = d % 10;
                            seen[d] = 1;
                        }
                    isSeen = func(seen);
                    if (isSeen == true){
                        myFile << "Case #" << i+1 << ": " << num << endl;
                        allSeen = true;
                    }
                }
                else if (num >=100 and num <=999){
                    for (int i = 2; i >=0; i--)
                        {
                            d = num/myArray[i];
                            d = d % 10;
                            seen[d] = 1;
                        }
                    isSeen = func(seen);
                    if (isSeen == true){
                        myFile << "Case #" << i+1 << ": " << num << endl;
                        allSeen = true;
                    }
                }
                else if (num >=1000 and num <=9999){
                    for (int i = 3; i >=0; i--)
                        {
                            d = num/myArray[i];
                            d = d % 10;
                            seen[d] = 1;
                        }

                    isSeen = func(seen);
                    if (isSeen == true){
                        myFile << "Case #" << i+1 << ": " << num << endl;
                        allSeen = true;
                    }
                }
                else if (num >=10000 and num <=99999){
                    for (int i = 4; i >=0; i--)
                        {
                            d = num/myArray[i];
                            d = d % 10;
                            seen[d] = 1;
                        }

                    isSeen = func(seen);
                    if (isSeen == true){
                        myFile << "Case #" << i+1 << ": " << num << endl;
                        allSeen = true;
                    }
                }
                else if (num >=100000 and num <=999999){
                    for (int i = 5; i >=0; i--)
                        {
                            d = num/myArray[i];
                            d = d % 10;
                            seen[d] = 1;
                        }

                    isSeen = func(seen);
                    if (isSeen == true){
                        myFile << "Case #" << i+1 << ": " << num << endl;
                        allSeen = true;
                    }
                }
                else if (num >=1000000 and num <=9999999){
                    for (int i = 6; i >=0; i--)
                        {
                            d = num/myArray[i];
                            d = d % 10;
                            seen[d] = 1;
                        }

                    isSeen = func(seen);
                    if (isSeen == true){
                        myFile << "Case #" << i+1 << ": " << num << endl;
                        allSeen = true;
                    }
                }
                else if (num >=10000000 and num <=99999999){
                    for (int i = 7; i >=0; i--)
                        {
                            d = num/myArray[i];
                            d = d % 10;
                            seen[d] = 1;
                        }

                    isSeen = func(seen);
                    if (isSeen == true){
                        myFile << "Case #" << i+1 << ": " << num << endl;
                        allSeen = true;
                    }
                }
                num = multiplier * temp;
                multiplier++;
            }
        }
    }
    input.close();
    myFile.close();
    return 0;
}
bool func (int arr[]){
    for (int i = 0; i < 10; i++){
        if(arr[i] == 0){
            return false;
        }
    }
    return true;
}
