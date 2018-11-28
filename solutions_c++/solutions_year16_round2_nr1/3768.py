#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char * argv[])
{
    int n = 0;
    int cases = 0;

    char decode[2001];
    char crosses[2001];
    bool enough = false;
    char read[2001];
    char newline;
    bool letter = false;
    //int phone[666] = {};
    int length = 0;
    char ** check = new char*[10]{ "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
    int cancel = 0;
    int s = 0;
    int digits[10] = {};

    ifstream fin("A-small-attempt2 (1).in");
    ofstream fout("A.txt");

    bool ok = false;

    if(fin.is_open())
    {
        //cout << "Open" << endl;

        fin >> cases;
        fin >> noskipws >> newline;

        for(int onebyone = 1; onebyone <= cases; onebyone++)
        {
            //length = 0;
            for(int i = 0; i < 10; i++)
            {
                digits[i] = 0;
            }
            for(int i = 0; i < 2001; i++)
            {
                read[i] = '\0';
            }

            fout << "Case #" << onebyone << ": ";
            //cout << "Case #" << onebyone << ": ";

            fin.getline(read,2000,'\n');
            //cout << read << endl;

            enough = false;

            for(int l = 0; read[l] != '\0'; l++)
            {
                if(read[l] == 'X')
                {
                    for(int i = 0; check[6][i] != '\0'; i++)
                    {
                        ok = false;
                        for(int again = 0; read[again] != '\0' && !ok; again++)
                        {
                            if(read[again] == check[6][i])
                            {
                                read[again] = '.';
                                ok = true;
                            }
                        }
                    }
                    digits[6]++;
                    length++;
                }
                else if(read[l] == 'W')
                {
                    for(int i = 0; check[2][i] != '\0'; i++)
                    {
                        ok = false;
                        for(int again = 0; read[again] != '\0' && !ok; again++)
                        {
                            if(read[again] == check[2][i])
                            {
                                read[again] = '.';
                                ok = true;
                            }
                        }
                    }
                    digits[2]++;
                    length++;
                }
                else if(read[l] == 'U')
                {
                    for(int i = 0; check[4][i] != '\0'; i++)
                    {
                        ok = false;
                        for(int again = 0; read[again] != '\0' && !ok; again++)
                        {
                            if(read[again] == check[4][i])
                            {
                                read[again] = '.';
                                ok = true;
                            }
                        }
                    }
                    digits[4]++;
                    length++;
                }
            }

            for(int sorry = 0;sorry < 10 && !enough; sorry++)
            {
                s = sorry;
                length = 0;
                for(int i = 0; i < 2000; i++)
                {
                    decode[i] = read[i];
                    crosses[i] = read[i];
                }
            for(int eng = sorry; eng < 10; eng++)
            {
                for(int i = 0; decode[i] != '\0'; i++)
                {
                    crosses[i] = decode[i];
                }
                letter = true;
                for(int l = 0; check[eng][l] != '\0' && letter; l++)
                {
                    letter = false;
                    for(int cross = 0; crosses[cross] != '\0' && !letter; cross++)
                    {
                        if(check[eng][l] == crosses[cross])
                        {
                            crosses[cross] = '.';
                            letter = true;
                        }
                    }
                }
                if(letter)
                {
                    for(int i = 0; crosses[i] != '\0'; i++)
                    {
                        decode[i] = crosses[i];
                    }
                    digits[eng]++;
                    length++;
                    eng--;
                }
            }
            enough = true;
            for(int i = 0; decode[i] != '\0' && enough; i++)
            {
                if(decode[i] != '.')
                {
                    enough = false;
                }
            }
            }

            for(int i = 0; i < 10; i++)
            {
                for(int j = 0; j < digits[i]; j++)
                {
                    fout << i;
                }
            }

            //for(int i = 0; i < length; i++)
            //{
            //    fout << phone[i];
            //}
            fout << endl;
        }

        fin.close();
        fout.close();
    }
    else
    {
        //cout << "Error opening file" << endl;
    }
    delete[] decode;
    return 0;
}
