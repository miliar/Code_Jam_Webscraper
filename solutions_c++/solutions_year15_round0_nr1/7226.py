
    #include<bits/stdc++.h>
    using namespace std;
    main()
    {
   freopen("a.txt","r",stdin);
   freopen("b.out","w",stdout);
	  int t,m=1;
	  cin>>t;
	  while(t--)
      {
              register int n,ind=-1,s=0,i;
              cin>>n;
              string s1;
              cin>>s1;
              register int a[n+1],ans=0;
              for(i=0;i<=n;i++)
              {
                  a[i]=s1[i]-'0';
              }
                for(i=0;i<=n;i++)
                {
                    s=s+a[i];
                    if(a[i]==0 && s<=i)
                    {
                        ans+=1;
                        s=s+1;
                    }

                }
              cout<<"Case #"<<m++<<": ";
              cout<<ans<<endl;
    }
    fclose(stdout);
    }
