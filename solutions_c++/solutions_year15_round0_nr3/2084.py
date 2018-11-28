#include <cstdio>

int L,X;
char pole[10005];

bool BruteForce(int start, int stav, int q, int z)
{
    //printf("BruteForce(%d,%d)\n", start,stav);
    char znak;
    while(start < L*X)
    {
        znak = pole[start%L];
        if(q == '1')
        {
            if(znak == '1')
            {
                ;
            }
            else if(znak == 'i')
            {
                q = 'i';
            }
            else if(znak == 'j')
            {
                q = 'j';
            }
            else
            {
                q = 'k';
            }
        }
        else if(q == 'i')
        {
            if(znak == '1')
            {
                ;
            }
            else if(znak == 'i')
            {
                q = '1';
                z = !z;
            }
            else if(znak == 'j')
            {
                q = 'k';
            }
            else
            {
                q = 'j';
                z = !z;
            }
        }
        else if(q == 'j')
        {
            if(znak == '1')
            {
                ;
            }
            else if(znak == 'i')
            {
                q = 'k';
                z = !z;
            }
            else if(znak == 'j')
            {
                q = '1';
                z = !z;
            }
            else
            {
                q = 'i';
            }
        }
        else
        {
            if(znak == '1')
            {
                ;
            }
            else if(znak == 'i')
            {
                q = 'j';
            }
            else if(znak == 'j')
            {
                q = 'i';
                z = !z;
            }
            else
            {
                q = '1';
                z = !z;
            }
        }

        if(q == 'i' && z == true && stav == 1)
        {
            if(BruteForce(start+1, 2, '1', true) == true)
            {
                //printf("1) OK\n");
                return true;
            }
        }
        if(q == 'j' && z == true && stav == 2)
        {
            if(BruteForce(start+1, 3, '1', true) == true)
            {
                //printf("2) OK\n");
                return true;
            }
        }
        if(q == 'k' && z == true && stav == 3 && start == L*X-1)
        {
            //printf("3) OK\n");
            return true;
        }

        start++;
    }
    return false;
}

void Testuj(int poradi)
{
    scanf("%d%d\n", &L, &X);

    char znak;
    char q = '1';
    bool z = true;

    for(int i=0; i<L; i++)
    {
        znak = getchar();
        pole[i] = znak;
        if(q == '1')
        {
            if(znak == '1')
            {
                ;
            }
            else if(znak == 'i')
            {
                q = 'i';
            }
            else if(znak == 'j')
            {
                q = 'j';
            }
            else
            {
                q = 'k';
            }
        }
        else if(q == 'i')
        {
            if(znak == '1')
            {
                ;
            }
            else if(znak == 'i')
            {
                q = '1';
                z = !z;
            }
            else if(znak == 'j')
            {
                q = 'k';
            }
            else
            {
                q = 'j';
                z = !z;
            }
        }
        else if(q == 'j')
        {
            if(znak == '1')
            {
                ;
            }
            else if(znak == 'i')
            {
                q = 'k';
                z = !z;
            }
            else if(znak == 'j')
            {
                q = '1';
                z = !z;
            }
            else
            {
                q = 'i';
            }
        }
        else
        {
            if(znak == '1')
            {
                ;
            }
            else if(znak == 'i')
            {
                q = 'j';
            }
            else if(znak == 'j')
            {
                q = 'i';
                z = !z;
            }
            else
            {
                q = '1';
                z = !z;
            }
        }
    }

    //printf("vysledek: %d%c\n", z, q);

    znak = q;
    bool znamenko = z;
    for(int i=1; i<X; i++)
    {
        if(q == '1')
        {
            if(znak == '1')
            {
                ;
            }
            else if(znak == 'i')
            {
                q = 'i';
            }
            else if(znak == 'j')
            {
                q = 'j';
            }
            else
            {
                q = 'k';
            }
        }
        else if(q == 'i')
        {
            if(znak == '1')
            {
                ;
            }
            else if(znak == 'i')
            {
                q = '1';
                z = !z;
            }
            else if(znak == 'j')
            {
                q = 'k';
            }
            else
            {
                q = 'j';
                z = !z;
            }
        }
        else if(q == 'j')
        {
            if(znak == '1')
            {
                ;
            }
            else if(znak == 'i')
            {
                q = 'k';
                z = !z;
            }
            else if(znak == 'j')
            {
                q = '1';
                z = !z;
            }
            else
            {
                q = 'i';
            }
        }
        else
        {
            if(znak == '1')
            {
                ;
            }
            else if(znak == 'i')
            {
                q = 'j';
            }
            else if(znak == 'j')
            {
                q = 'i';
                z = !z;
            }
            else
            {
                q = '1';
                z = !z;
            }
        }

        if(znamenko == false)
        {
            z = !z;
        }

        //printf("...vysledek: %d%c\n", z, q);
    }

    //printf("vysledek: %d%c\n", z, q);
    if(q == '1' && z == false && L*X >= 3)
    {
        //printf("mozna...\n");
        if(BruteForce(0, 1, '1', true))
            printf("Case #%d: YES\n", poradi);
        else
            printf("Case #%d: NO\n", poradi);
    }
    else
    {
        printf("Case #%d: NO\n", poradi);
    }
}

int main()
{
    int T;
    scanf(" %d", &T);

    for(int i=1; i<=T; i++)
    {
        Testuj(i);
    }

    return 0;
}
