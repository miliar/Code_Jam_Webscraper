//
//  main.cpp
//  Tic-Tac-Toe-Tomek__CodeJam2013
//
//  Created by Marcin's Mac on 13.04.2013.
//  Copyright (c) 2013 Marcin's Mac. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <math.h>
using namespace std;

unsigned short int casetests;
string coutput [1002];
char icase [4][4];
bool mastercheck=false;
bool check=false;
bool emptycheck=false;

int main()
{
    cin>>casetests;
    int i = 0;
    int lines=0;
    int characters=0;
    while (i<casetests)
    {
        
        mastercheck=false;
        check=false;
        emptycheck=false;
        
        
        
        while (lines<4)
        {
            
            while (characters<4)
            {
                cin>>icase[lines][characters];
                characters++;
            }
            
            characters=0;
            lines++;
            
        }
        lines=0;
            while (lines<4)
            {
                if (icase[lines][0]=='X')
                {
                    if ((icase[lines][1]=='X' || icase[lines][1]=='T') && (icase[lines][2]=='X' || icase[lines][2]=='T') &&     (icase[lines][3]=='X' || icase[lines][3]=='T') )
                    {
                        coutput [i]="X won";
                        check=true;
                    }
                        
                }
                
                else if (icase[lines][0]=='O')
                {
                    if ((icase[lines][1]=='O' || icase[lines][1]=='T') && (icase[lines][2]=='O' || icase[lines][2]=='T') &&     (icase[lines][3]=='O' || icase[lines][3]=='T') )
                    {
                        coutput [i]="O won";
                        check=true;
                    }
                    
                }
                else if (icase[lines][0]=='T')
                {
                    if (icase[lines][1]=='X')
                    {
                        if ((icase[lines][2]=='X') && (icase[lines][3]=='X'))
                        {
                            coutput [i]="X won";
                            check=true;
                        }
                    }
                    else if (icase[lines][1]=='O')
                    {
                        if ((icase[lines][2]=='O') && (icase[lines][3]=='O'))
                        {
                            coutput [i]="O won";
                            check=true;
                        }
                    }
                }
                if (check==true) lines=4;
                else lines++;
            }
            
            if (check==false)
            {
                
                    while (characters<4)
                    {
                        if (icase[0][characters]=='X')
                        {
                            if ((icase[1][characters]=='X' || icase[1][characters]=='T') && (icase[2][characters]=='X' || icase[2][characters]=='T') &&     (icase[3][characters]=='X' || icase[3][characters]=='T') )
                            {
                                coutput [i]="X won";
                                check=true;
                            }
                            
                        }
                        
                        else if (icase[0][characters]=='O')
                        {
                            if ((icase[1][characters]=='O' || icase[1][characters]=='T') && (icase[2][characters]=='O' || icase[2][characters]=='T') &&     (icase[3][characters]=='O' || icase[3][characters]=='T') )
                            {
                                coutput [i]="O won";
                                check=true;
                            }
                            
                        }
                        else if (icase[0][characters]=='T')
                        {
                            if (icase[1][characters]=='X')
                            {
                                if ((icase[2][characters]=='X') && (icase[3][characters]=='X'))
                                {
                                    coutput [i]="X won";
                                    check=true;
                                }
                            }
                            else if (icase[1][characters]=='O')
                            {
                                if ((icase[2][characters]=='O') && (icase[3][characters]=='O'))
                                {
                                    coutput [i]="O won";
                                    check=true;
                                }
                            }
                        }
                        if (check==true) characters=4;
                        else characters++;
                    }

                }
            if (check==false)
            {
                if (icase[0][0]=='X')
                {
                    if ((icase[1][1]=='X' || icase[1][1]=='T') && (icase[2][2]=='X' || icase[2][2]=='T') &&     (icase[3][3]=='X' || icase[3][3]=='T') )
                    {
                        coutput [i]="X won";
                        check=true;
                    }
                    
                }
                else if (icase[0][0]=='O')
                {
                    if ((icase[1][1]=='O' || icase[1][1]=='T') && (icase[2][2]=='O' || icase[2][2]=='T') &&     (icase[3][3]=='O' || icase[3][3]=='T') )
                    {
                        coutput [i]="O won";
                        check=true;
                    }
                    
                }
                else if (icase[0][0]=='T')
                {
                    if (icase[1][1]=='X')
                    {
                        if ((icase[2][2]=='X') && (icase[3][3]=='X'))
                        {
                            coutput [i]="X won";
                            check=true;
                        }
                    }
                    else if (icase[1][1]=='O')
                    {
                        if ((icase[2][2]=='O') && (icase[3][3]=='O'))
                        {
                            coutput [i]="O won";
                            check=true;
                        }
                    }
                }

            }
            if (check==false)
            {
                if (icase[0][3]=='X')
                {
                    if ((icase[1][2]=='X' || icase[1][2]=='T') && (icase[2][1]=='X' || icase[2][1]=='T') &&     (icase[3][0]=='X' || icase[3][0]=='T') )
                    {
                        coutput [i]="X won";
                        check=true;
                    }
                    
                }
                else if (icase[0][3]=='O')
                {
                    if ((icase[1][2]=='O' || icase[1][2]=='T') && (icase[2][1]=='O' || icase[2][1]=='T') &&     (icase[3][0]=='O' || icase[3][0]=='T') )
                    {
                        coutput [i]="O won";
                        check=true;
                    }
                    
                }
                else if (icase[0][3]=='T')
                {
                    if (icase[1][2]=='X')
                    {
                        if ((icase[2][1]=='X') && (icase[3][0]=='X'))
                        {
                            coutput [i]="X won";
                            check=true;
                        }
                    }
                    else if (icase[1][2]=='O')
                    {
                        if ((icase[2][1]=='O') && (icase[3][0]=='O'))
                        {
                            coutput [i]="O won";
                            check=true;
                        }
                    }
                }

            }
            lines=0;
            characters=0;
            if (check==false)
            {
                while (lines<4)
                {
                    
                    while (characters<4)
                    {
                        if (icase[lines][characters]=='.')
                        {
                            emptycheck=true;
                            check=true;
                            coutput[i]="Game has not completed";
                            characters=4;
                        }
                        else characters++;
                    }
                    
                    characters=0;
                    if (emptycheck==true)
                    {
                        lines=4;
                    }
                    else lines++;
                    
                }
                if (emptycheck==false)
                {
                    coutput[i]="Draw";
                }
            }
            

        
        
        
        
        
        lines=0;
        characters=0;
        
        
        
        
        
        i++;
    }
    i=1;
    int j=0;
    while (i<=casetests)
    {
        cout<<"Case #"<<i<<": "<<coutput[j]<<endl;
        j++;
        i++;
    }
    
    
    
    
    getchar();
    cin.ignore();
    
    return 0;
}

