   #include <stdio.h>
   void main()
   {
     
      int N,k,d,small,p,t;
      float ke[1000];
      float na[1000],temp;
	   FILE *i,*o;
      i = fopen("ques.txt", "r");
      o = fopen("ans.txt", "w");

      fscanf(i, "%d\n", &t);

      for (int i1=1;i1<=t;i1++)
      {
          

         fscanf(i, "%d\n", &N);
          d=0;
          

         for(int j=0;j<N;j++)
         fscanf(i, "%f\n", &na[j]);
         for(int k=0;k<N;k++)
         fscanf(i, "%f\n", &ke[k]);
//for sorting
        for(int u=0;u<N-1;u++)
        {
        small=u;
        for(int v=u+1;v<N;v++)
        {
        if(na[small]>na[v])
        small=v;

        }
        temp=na[small];
        na[small]=na[u];
        na[u]=temp;
    
        }


        for(int u=0;u<N-1;u++)
        {
        small=u;
        for(int v=u+1;v<N;v++)
        {
        if(ke[small]>ke[v])
        small=v;

        }
        temp=ke[small];
        ke[small]=ke[u];
        ke[u]=temp;
    
        }
k=0;
        for(int l=0;l<N;l++)
         {
         if(na[l]>ke[k])
         {
         d++;
         k++;
         }
         }


int c=0;
p=0;
        for(int n=p;n<N;n++)
        {
            if(ke[n]>na[c])
            {
                p=n+1;
                c++;
            }

        }

  


        fprintf(o, "Case #%d: %d %d\n", i1,d,N-c);
}
      fclose(i);
      fclose(o);
   }
