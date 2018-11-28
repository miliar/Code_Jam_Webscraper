    #include<cstdio>
     
    using namespace std;
    typedef double d;
    int TC;
    d C,F,X,total,temp,temp2, speed,jawab;
    int i,stat,count=0;
    
    double Hitung(float F)
    {
    temp2 = total; // Tampung Sementara
     
    total += (X / (F/10)) / 10; // For Continuosly
    if(temp < total) stat = 1;
    return total;
    }
     
    double cari(){
    	stat = 0;
    total = 0;
    speed = 2;
    temp2 = 0;
    temp = (X / 0.2) / 10;
    while(stat == 0)
    {
    total = temp2;
    total += (C / (speed / 10)) / 10;
    speed = speed + F;
    total = Hitung(speed);
    if(stat == 1) break;
    temp = total;
    }
    return temp;
    }
    int main()
    {
    scanf("%d",&TC);
    for(i = 1; i <= TC; i++)
    {
    scanf("%lf %lf %lf",&C,&F,&X);
    jawab = cari();
    printf("Case #%d: %.7lf\n",i,temp);
    }
     
    return 0;
    }
