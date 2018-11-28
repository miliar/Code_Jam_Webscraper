#include <stdio.h>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

char group[8] = {'1','i','j','k','I','J','K','-'};

char table[8][8] = {
{'1','i','j','k','I','J','K','-'},
{'i','-','k','J','1','K','j','I'},
{'j','K','-','i','k','1','I','J'},
{'k','j','I','-','J','i','1','K'},
{'I','1','K','j','-','k','J','i'},
{'J','k','1','I','K','-','i','j'},
{'K','J','i','1','j','I','-','k'},
{'-','I','J','K','i','j','k','1'},
};

string str;

bool ijk(int numChar, int numTimes)
{
    bool have_i = false , have_j = false , have_k = false;
    char aux1,aux2;
    int cont1,cont2,tam;
    string backup;

    for(int i =0 ; i < numTimes ; i++)
        backup += str;
    reverse(backup.begin(),backup.end());
    //printf("%s\n",backup.c_str());
    tam = backup.size();

    for(int i = 1; i < tam ; i++)
    {
        //Procura o i e retira-o caso ache
        if(!have_i && backup.size()!=0)
        {
            if(backup.back() == 'i')
            {
                backup.pop_back();
                have_i = true;
            }
            else
            {
                aux1 = backup.back();
                backup.pop_back();
                aux2 = backup.back();
                backup.pop_back();

                for(int j = 0 ; j < 8 ; j++)
                {
                    if(group[j] == aux1)
                        cont1 = j;
                    if(group[j] == aux2)
                        cont2 = j;
                }

                backup.push_back(table[cont1][cont2]);
            }
        }
        else
        {
            //Depois do i vem o j...Mesma coisa
            if(!have_j && backup.size()!=0)
            {
                if(backup.back() == 'j')
                {
                    backup.pop_back();
                    have_j = true;
                }
                else
                {
                    aux1 = backup.back();
                    backup.pop_back();
                    aux2 = backup.back();
                    backup.pop_back();

                    for(int j = 0 ; j < 8 ; j++)
                    {
                        if(group[j] == aux1)
                            cont1 = j;
                        if(group[j] == aux2)
                            cont2 = j;
                    }

                    backup.push_back(table[cont1][cont2]);
                }
            }
            else
            {
                //Pro k tbm
                if(!have_k && backup.size()!=0)
                {
                    if(backup.back() == 'k')
                    {
                        backup.pop_back();
                        have_k = true;
                    }
                    else
                    {
                        aux1 = backup.back();
                        backup.pop_back();
                        aux2 = backup.back();
                        backup.pop_back();

                        for(int j = 0 ; j < 8 ; j++)
                        {
                            if(group[j] == aux1)
                                cont1 = j;
                            if(group[j] == aux2)
                                cont2 = j;
                        }

                        backup.push_back(table[cont1][cont2]);
                    }
                }
                //caso tenha coisas extra
                else
                {
                    //if(backup.back() == '1')
                    //{
                        //backup.pop_back();
                    //}
                    //else
                    {
                        aux1 = backup.back();
                        backup.pop_back();
                        aux2 = backup.back();
                        backup.pop_back();

                        for(int j = 0 ; j < 8 ; j++)
                        {
                            if(group[j] == aux1)
                                cont1 = j;
                            if(group[j] == aux2)
                                cont2 = j;
                        }

                        backup.push_back(table[cont1][cont2]);
                    }
                }
            }
        }
        //printf("%s\n",backup.c_str());
    }

    if(have_i && have_j && have_k && backup.back() == '1')
        return true;
    else if(backup.back()=='k' && have_i && have_j && !have_k)
        return true;
    else
        return false;
}


int main()
{
    int numTimes,testes,numChar;

    scanf("%d", &testes);
    for(int i = 0; i < testes ; i++)
    {
        scanf("%d %d\n", &numChar,&numTimes);
        getline(cin,str);

        if(ijk(numChar,numTimes))
            printf("Case #%d: YES\n",i+1);
        else
            printf("Case #%d: NO\n",i+1);

    }

    return 0;
}
