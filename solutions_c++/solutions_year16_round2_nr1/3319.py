#include <iostream>
#include <string>
#include <cstring>
#include <fstream>
#include <cstdlib>
#include <algorithm>
#include <list>

using namespace std;

int main()
{
    ifstream fin;
    ofstream fout;

    fin.open("A-large.in", ios::in);
    if (!fin.is_open())
    {
        cerr << "Unable to open file 'A-sample'" << endl;
        exit(10);
    }

    fout.open("A-large-answer.txt", ios::out);
    if(!fout.is_open())
    {
        cerr << "Unable to open file 'A-sample-answer'" << endl;
        exit(10);
    }

    int T, counter;
    string zero = "ZERO";
    string one = "ONE";
    string two = "TWO";
    string three = "THREE";
    string four = "FOUR";
    string five = "FIVE";
    string six = "SIX";
    string seven = "SEVEN";
    string eight = "EIGHT";
    string nine = "NINE";
    string stringPhone;
    string::iterator iterStringPhone;
    string::iterator iterDigit;
    string::iterator clone;


    fin >> T;

    for (int i = 0; i < T; i++){
        fin >> stringPhone;
        string phone;

        for (iterStringPhone = stringPhone.begin(); iterStringPhone != stringPhone.end(); iterStringPhone++){
            if (*iterStringPhone == 'Z'){
                phone = phone + '0';
                for (iterDigit = zero.begin(); iterDigit != zero.end(); iterDigit++){
                    for (clone = stringPhone.begin(); clone != stringPhone.end(); clone++){
                        if(*clone == *iterDigit){
                            *clone = 'a';
                            //clone = stringPhone.end();
                            break;
                        }
                    }

                }
            }
        }
        for (iterStringPhone = stringPhone.begin(); iterStringPhone != stringPhone.end(); iterStringPhone++){
            if (*iterStringPhone == 'W'){
                phone = phone + '2';
                for (iterDigit = two.begin(); iterDigit != two.end(); iterDigit++){
                    for (clone = stringPhone.begin(); clone != stringPhone.end(); clone++){
                        if(*clone == *iterDigit){
                            *clone = 'a';
                            //clone = stringPhone.end();
                            break;
                        }
                    }
                }
            }
        }
        for (iterStringPhone = stringPhone.begin(); iterStringPhone != stringPhone.end(); iterStringPhone++){
            if (*iterStringPhone == 'U'){
                phone = phone + '4';
                for (iterDigit = four.begin(); iterDigit != four.end(); iterDigit++){
                    for (clone = stringPhone.begin(); clone != stringPhone.end(); clone++){
                        if(*clone == *iterDigit){
                            *clone = 'a';
                            //clone = stringPhone.end();
                            break;
                        }
                    }
                }
            }
        }
        for (iterStringPhone = stringPhone.begin(); iterStringPhone != stringPhone.end(); iterStringPhone++){
            if (*iterStringPhone == 'X'){
                phone = phone + '6';
                for (iterDigit = six.begin(); iterDigit != six.end(); iterDigit++){
                    for (clone = stringPhone.begin(); clone != stringPhone.end(); clone++){
                        if(*clone == *iterDigit){
                            *clone = 'a';
                            //clone = stringPhone.end();
                            break;
                        }
                    }
                }
            }
        }
        for (iterStringPhone = stringPhone.begin(); iterStringPhone != stringPhone.end(); iterStringPhone++){
            if (*iterStringPhone == 'G'){
                phone = phone + '8';
                for (iterDigit = eight.begin(); iterDigit != eight.end(); iterDigit++){
                     for (clone = stringPhone.begin(); clone != stringPhone.end(); clone++){
                        if(*clone == *iterDigit){
                            *clone = 'a';
                            //clone = stringPhone.end();
                            break;
                        }
                    }
                }
            }
        }

        for (iterStringPhone = stringPhone.begin(); iterStringPhone != stringPhone.end(); iterStringPhone++){
            if (*iterStringPhone == 'O'){
                phone = phone + '1';
                for (iterDigit = one.begin(); iterDigit != one.end(); iterDigit++){

                    for (clone = stringPhone.begin(); clone != stringPhone.end(); clone++){
                        if(*clone == *iterDigit){
                            *clone = 'a';
                            //clone = stringPhone.end();
                            break;
                        }
                    }
                }
            }
        }
        for (iterStringPhone = stringPhone.begin(); iterStringPhone != stringPhone.end(); iterStringPhone++){
            if (*iterStringPhone == 'T'){
                phone = phone + '3';
                for (iterDigit = three.begin(); iterDigit != three.end(); iterDigit++){
                    for (clone = stringPhone.begin(); clone != stringPhone.end(); clone++){
                        if(*clone == *iterDigit){
                            *clone = 'a';
                            //clone = stringPhone.end();
                            break;
                        }
                    }
                }
            }
        }
        for (iterStringPhone = stringPhone.begin(); iterStringPhone != stringPhone.end(); iterStringPhone++){
            if (*iterStringPhone == 'F'){
                phone = phone + '5';
                for (iterDigit = five.begin(); iterDigit != five.end(); iterDigit++){
                    for (clone = stringPhone.begin(); clone != stringPhone.end(); clone++){
                        if(*clone == *iterDigit){
                            *clone = 'a';
                            //clone = stringPhone.end();
                            break;
                        }
                    }
                }
            }
        }
        for (iterStringPhone = stringPhone.begin(); iterStringPhone != stringPhone.end(); iterStringPhone++){
            if (*iterStringPhone == 'S'){
                phone = phone + '7';
                for (iterDigit = seven.begin(); iterDigit != seven.end(); iterDigit++){
                     for (clone = stringPhone.begin(); clone != stringPhone.end(); clone++){
                        if(*clone == *iterDigit){
                            *clone = 'a';
                            //clone = stringPhone.end();
                            break;
                        }
                    }
                }
            }
        }
        for (iterStringPhone = stringPhone.begin(); iterStringPhone != stringPhone.end(); iterStringPhone++){
            if (*iterStringPhone == 'I'){
                phone = phone + '9';
                for (iterDigit = nine.begin(); iterDigit != nine.end(); iterDigit++){
                    for (clone = stringPhone.begin(); clone != stringPhone.end(); clone++){
                        if(*clone == *iterDigit){
                            *clone = 'a';
                            //clone = stringPhone.end();
                            break;
                        }
                    }
                }
            }
        }
        sort(phone.begin(), phone.end());

        fout << "Case #" << i+1 << ": " << phone << endl;
    }

    fin.close();
    fout.close();


    return 0;
}
