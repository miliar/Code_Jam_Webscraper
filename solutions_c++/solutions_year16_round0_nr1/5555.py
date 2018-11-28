/*
#include "iostream"
#include "vector"
#include "map"
#include "climits"
#include "queue"
#include "algorithm"
#include "set"
#include "cmath"
#include "cstring"
#include "stack"

using namespace std;
long long int i,j,k,l,n,m,p,q,a[111111],r;
long long int finalAns;
string s;
long long int disFromRoot[111111],parent[111111],ans[111111],lca[111111][20],level[111111],subtreeNode[111111],deepestPath[111111],deepestNode[111111];
vector< vector< pair<long long int,long long int> > >tree;


long long int treeSize[111111],baseArray[111111],headOfChain[111111],chainNo,indexInChain[111111],headOfNode[111111],edgeStore[111111];
pair< long long ,long long > pathStore[111111];

void findParentAndDis(long long currentNode,long long currentNodeParent,long long distanceFromRoot,long long levelOfNode){
    disFromRoot[currentNode]=distanceFromRoot;
    parent[currentNode]=currentNodeParent;
    level[currentNode]=levelOfNode;
    
    treeSize[currentNode]=1;
    deepestPath[currentNode]=0;
    deepestNode[currentNode]=currentNode;
    for(int fp=0;fp<tree[currentNode].size();fp++){
        if(tree[currentNode][fp].first!=currentNodeParent){
            findParentAndDis(tree[currentNode][fp].first, currentNode, distanceFromRoot+tree[currentNode][fp].second,levelOfNode+1);
            treeSize[currentNode]+=treeSize[tree[currentNode][fp].first];
            if(tree[currentNode][fp].second+deepestPath[tree[currentNode][fp].first]>deepestPath[currentNode]){
                deepestPath[currentNode]=tree[currentNode][fp].second+deepestPath[tree[currentNode][fp].first];
                deepestNode[currentNode]=deepestNode[tree[currentNode][fp].first];
            }
        }
    }
    
    return;
}

long long lcaQuery(long long X,long long Y){
    if(X==Y)return X;
    
    long long logs,li;
    
    if(level[X]<level[Y])swap(X,Y);
    
    for(logs=1;1<<logs<=level[X];logs++){
    }
    
    logs--;
    for(li=logs;li>=0;li--){
        if(level[X]-(1<<li)>=level[Y]){
            X=lca[X][li];
        }
    }
    if(X==Y)return X;
    
    for(li=logs;li>=0;li--){
        if(lca[X][li]!=-1 && lca[X][li]!=lca[Y][li]){
            X=lca[X][li];
            Y=lca[Y][li];
        }
    }
    return parent[X];
}

// decomposing in sorted chain

void heavyLightDecomposition(long long int currentNode,long long int parentNode,long long int chainIndex,long long weight){
//    cout<<"currentNode "<<currentNode<<" parentnode "<<parentNode<<" chainindex "<<chainIndex<<" weight "<<weight<<endl;
    if(chainIndex==0){
        headOfChain[++chainNo]=k+1;
    }
    indexInChain[currentNode]=chainIndex;
    baseArray[k+1]=weight+(chainIndex>0?baseArray[k]:0LL);
    headOfNode[currentNode]=chainNo;
    edgeStore[k+1]=currentNode;
    k++;
    long long maxIndex=-1,maxSize=-1;
    
    for(int hld=0;hld<tree[currentNode].size();hld++){
        if(tree[currentNode][hld].first!=parentNode){
            if(treeSize[tree[currentNode][hld].first]>maxSize){
                maxSize=treeSize[tree[currentNode][hld].first];
                maxIndex=hld;
            }
        }
    }
//    cout<<"maxindex "<<maxIndex<<" maxsize "<<maxSize<<endl;
    if(maxSize>-1){
        heavyLightDecomposition(tree[currentNode][maxIndex].first, currentNode, chainIndex+1, tree[currentNode][maxIndex].second);
    }
    
    for(int hld=0;hld<tree[currentNode].size();hld++){
        if(tree[currentNode][hld].first!=parentNode && hld!=maxIndex){
            heavyLightDecomposition(tree[currentNode][hld].first, currentNode, 0, tree[currentNode][hld].second);
        }
    }
    return;
}

long long queryHld(long long downNode,long long upNode,long long additionalWeight){   //returns node
    long long res=-1;// node
    cout<<"downnode "<<downNode<<" upnode "<<upNode<<" adweight "<<additionalWeight<<endl;
    while(true){
        if(headOfNode[downNode]==headOfNode[upNode]){
            long long right=headOfChain[headOfNode[downNode]]+indexInChain[downNode];
            long long left=headOfChain[headOfNode[downNode]]+indexInChain[upNode];
            
            long long mid=(left+right)/2;
        //    long long addition=disFromRoot[edgeStore[left]]-disFromRoot[parent[upNode]];
            long long addition=disFromRoot[parent[headOfNode[upNode]]];
            cout<<"addition "<<addition<<" edgeleft "<<left<<" edgeright "<<right<<" edgestore "<<edgeStore[left]<<" parupnode "<<upNode<<endl;

            //needs to find min(addition+additionalWeight+dis[upnode,j])>=deepest[j]
            while(left<=right){   //binary search
                if(additionalWeight+disFromRoot[parent[edgeStore[mid]]]-disFromRoot[parent[upNode]]<addition*(left-mid+1)+baseArray[mid]-(mid==0?0LL:baseArray[mid-1])+deepestPath[edgeStore[mid]]){  // need to multiply here with addition
                    left=mid+1;
                    res=mid;
                }
                else{
                    right=mid-1;
                }
                mid=(left+right)/2;
            }
            cout<<"res "<<edgeStore[res]<<endl;
            break;
        }
        long long right=headOfChain[headOfNode[downNode]]+indexInChain[downNode];
        long long left=headOfChain[headOfNode[downNode]];
        
        long long mid=(left+right)/2;
     //   long long addition=disFromRoot[edgeStore[left]]-disFromRoot[parent[upNode]];
        long long addition=disFromRoot[parent[headOfNode[upNode]]];
    //    cout<<"addition "<<addition<<endl;
        //needs to find min(addition+additionalWeight+dis[upnode,j])>=deepest[j]
        while(left<=right){   //binary search
            if(additionalWeight+disFromRoot[parent[edgeStore[mid]]]-disFromRoot[parent[upNode]]<addition*(left-mid+1)+baseArray[mid]-(mid==0?0LL:baseArray[mid-1])+deepestPath[edgeStore[mid]]){  // need to multiply here with addition
                left=mid+1;
                res=mid;
            }
            else{
                right=mid-1;
            }
            mid=(left+right)/2;
        }
        
        if(res==headOfChain[headOfNode[downNode]]){
            downNode=parent[downNode];
        }
        else break;
    }
    return edgeStore[res];
}




void solveByDFS(long long currentNode,long long parentNode){
    if(tree[currentNode].size()==1){
        ans[currentNode]=0;
        subtreeNode[currentNode]=currentNode;
        pathStore[currentNode]={currentNode,currentNode};
        return;
    }
    
    long long firstMax,secondMax,firstMaxIndex,secondMaxIndex;
    firstMax=secondMax=0;firstMaxIndex=secondMaxIndex=-1;
    
    for(int si=0;si<tree[currentNode].size();si++){
        if(tree[currentNode][si].first!=parentNode){
            if(tree[currentNode][si].second+deepestPath[tree[currentNode][si].first]>firstMax){
                secondMax=firstMax;
                secondMaxIndex=firstMaxIndex;
                firstMaxIndex=si;
                firstMax=tree[currentNode][si].second+deepestPath[tree[currentNode][si].first];
            }
            else if(tree[currentNode][si].second+deepestPath[tree[currentNode][si].first]>secondMax){
                secondMax=tree[currentNode][si].second+deepestPath[tree[currentNode][si].first];
                secondMaxIndex=si;
            }
        }
    }
    
    ans[currentNode]=firstMax;subtreeNode[currentNode]=currentNode;
    pathStore[currentNode]={currentNode,deepestNode[currentNode]};
    cout<<"currentnode "<<currentNode<<" parentnode "<<parentNode<<" pathstore first "<<pathStore[currentNode].first<<" second "<<pathStore[currentNode].second<<endl;
    
    for(int si=0;si<tree[currentNode].size();si++){
        if(tree[currentNode][si].first!=parentNode){
            solveByDFS(tree[currentNode][si].first, currentNode);
            cout<<"subcrrent node "<<tree[currentNode][si].first<<" currentnode "<<currentNode<<" currentminmax "<<ans[currentNode]<<endl;
            cout<<"its path "<<pathStore[tree[currentNode][si].first].first<<" "<<pathStore[tree[currentNode][si].first].second<<endl;
            if(si==firstMaxIndex){
                //check longest path of subtreenode[tree[currentnode][si].first
                //if its equal to ans[tree[currentnode][si].first] then ans[currentnode]=min(ans[currentnode],ans[tree[currentnode[si].first]])
                //else find node j from path currentnode->tree[currentnode[si].first such that dis[i,j]+secondmax>=deepestpath[j]
                /*
                if(ans[tree[currentNode][si].first]>=disFromRoot[tree[currentNode][si].first]-disFromRoot[currentNode]+secondMax){
                    if(ans[currentNode]>ans[tree[currentNode][si].first]){
                        ans[currentNode]=ans[tree[currentNode][si].first];
                        subtreeNode[currentNode]=subtreeNode[tree[currentNode][si].first];
                    }
                }
                else{
                    long long nod=queryHld(subtreeNode[tree[currentNode][si].first], tree[currentNode][si].first, secondMax);
                    if(nod!=-1){
                        if(ans[currentNode]>disFromRoot[nod]-disFromRoot[currentNode]+secondMax){
                            ans[currentNode]=disFromRoot[nod]-disFromRoot[currentNode]+secondMax;
                            subtreeNode[currentNode]=nod;
                        }
                    }
                }
 
                
                long long templca=lcaQuery(pathStore[tree[currentNode][si].first].first, pathStore[tree[currentNode][si].first].second);
                
                if(templca==pathStore[tree[currentNode][si].first].first || templca==pathStore[tree[currentNode][si].first].second){
                    long long tempnode;
                    if(templca==pathStore[tree[currentNode][si].first].first){
                        tempnode=pathStore[tree[currentNode][si].first].second;
                    }
                    else tempnode=pathStore[tree[currentNode][si].first].first;
                    long long nod=queryHld(tempnode,tree[currentNode][si].first, secondMax);
      //              cout<<"watching A nod "<<nod<<" child "<<tree[currentNode][si].first<<" currentnode "<<currentNode<<" currentpath first "
      //                          <<pathStore[currentNode].first<<" second "<<pathStore[currentNode].second<<endl;
                    if(nod!=-1){
                        if(ans[currentNode]>deepestPath[parent[nod]]){
                            ans[currentNode]=deepestPath[parent[nod]];
                            //assign path
                            pathStore[currentNode]={parent[nod],deepestNode[parent[nod]]};
                        }
                        if(ans[currentNode]>disFromRoot[nod]-disFromRoot[currentNode]+secondMax){
                            ans[currentNode]=disFromRoot[nod]-disFromRoot[currentNode]+secondMax;
                            //assign path
                            if(secondMaxIndex==-1)
                                pathStore[currentNode]={currentNode,nod};
                            else
                                pathStore[currentNode]={nod,deepestNode[tree[currentNode][secondMaxIndex].first]};

                        }
                    }
                }
                else{
                    if(disFromRoot[templca]-disFromRoot[currentNode]+secondMax<disFromRoot[pathStore[tree[currentNode][si].first].second]){
                        if(ans[currentNode]>ans[tree[currentNode][si].first]){
                            ans[currentNode]=ans[tree[currentNode][si].first];
                            //assign path
                            pathStore[currentNode]=pathStore[tree[currentNode][si].first];
                        }
                    }
                    else{
                        long long nod=queryHld(pathStore[tree[currentNode][si].first].first, tree[currentNode][si].first, secondMax);
                        if(nod!=-1){
                            if(ans[currentNode]>deepestPath[parent[nod]]){
                                ans[currentNode]=deepestPath[parent[nod]];
                                //assign path
                                pathStore[currentNode]={parent[nod],deepestNode[parent[nod]]};

                            }
                            if(ans[currentNode]>disFromRoot[nod]-disFromRoot[currentNode]+secondMax){
                                ans[currentNode]=disFromRoot[nod]-disFromRoot[currentNode]+secondMax;
                                //assign path
                                if(secondMaxIndex==-1)
                                    pathStore[currentNode]={currentNode,nod};
                                else
                                    pathStore[currentNode]={nod,deepestNode[tree[currentNode][secondMaxIndex].first]};
                            }
                        }
                    }
                }
                
            }
            else{
                /*
                if(ans[tree[currentNode][si].first]>=disFromRoot[tree[currentNode][si].first]-disFromRoot[currentNode]+firstMax){
                    if(ans[currentNode]>ans[tree[currentNode][si].first]){
                        ans[currentNode]=ans[tree[currentNode][si].first];
                        subtreeNode[currentNode]=subtreeNode[tree[currentNode][si].first];
                    }
                }
                else{
                    long long nod=queryHld(subtreeNode[tree[currentNode][si].first], tree[currentNode][si].first, firstMax);
                    if(nod!=-1){
                        if(ans[currentNode]>disFromRoot[nod]-disFromRoot[currentNode]+secondMax){
                            ans[currentNode]=disFromRoot[nod]-disFromRoot[currentNode]+secondMax;
                            subtreeNode[currentNode]=nod;
                        }
                    }
                }
 
                long long templca=lcaQuery(pathStore[tree[currentNode][si].first].first, pathStore[tree[currentNode][si].first].second);
                
                if(templca==pathStore[tree[currentNode][si].first].first || templca==pathStore[tree[currentNode][si].first].second){
                    long long tempnode;
                    if(templca==pathStore[tree[currentNode][si].first].first){
                        tempnode=pathStore[tree[currentNode][si].first].second;
                    }
                    else tempnode=pathStore[tree[currentNode][si].first].first;
                    long long nod=queryHld(tempnode,tree[currentNode][si].first, firstMax);
                    cout<<"second nod "<<nod<<endl;
                    if(nod!=-1){
                        if(ans[currentNode]>deepestPath[parent[nod]]){
                            ans[currentNode]=disFromRoot[deepestPath[parent[nod]]];
                            //assign path
                            pathStore[currentNode]={parent[nod],deepestNode[parent[nod]]};

                        }
                        if(ans[currentNode]>disFromRoot[nod]-disFromRoot[currentNode]+firstMax){
                            ans[currentNode]=disFromRoot[nod]-disFromRoot[currentNode]+firstMax;
                            //assign path
                            pathStore[currentNode]={nod,deepestNode[tree[currentNode][firstMaxIndex].first]};

                        }
                    }
                }
                else{
                    if(disFromRoot[templca]-disFromRoot[currentNode]+firstMax<disFromRoot[pathStore[tree[currentNode][si].first].second]){
                        if(ans[currentNode]>ans[tree[currentNode][si].first]){
                            ans[currentNode]=ans[tree[currentNode][si].first];
                            //assign path
                            pathStore[currentNode]=pathStore[tree[currentNode][si].first];

                        }
                    }
                    else{
                        long long nod=queryHld(pathStore[tree[currentNode][si].first].first, tree[currentNode][si].first, firstMax);
                        if(nod!=-1){
                            if(ans[currentNode]>deepestPath[parent[nod]]){
                                ans[currentNode]=disFromRoot[deepestPath[parent[nod]]];
                                //assign path
                                pathStore[currentNode]={parent[nod],deepestNode[parent[nod]]};

                            }
                            if(ans[currentNode]>disFromRoot[nod]-disFromRoot[currentNode]+firstMax){
                                ans[currentNode]=disFromRoot[nod]-disFromRoot[currentNode]+firstMax;
                                //assign path
                                pathStore[currentNode]={nod,deepestNode[tree[currentNode][firstMaxIndex].first]};

                            }
                        }
                    }
                }
            }
        }
    }
    cout<<"finalcurrentnode "<<currentNode<<" final ans "<<ans[currentNode]<<" pathstore "<<pathStore[currentNode].first<<" "<<pathStore[currentNode].second<<endl;
}

int main(){
    int t;
    scanf("%d",&t);
    while(t--){
        scanf("%lld",&n);
        tree.clear();
        for(i=0;i<=n;i++){
            tree.push_back(vector< pair<long long int,long long int> >());
        }
        for(i=0;i<n-1;i++){
            scanf("%lld%lld%lld",&p,&q,&r);
            tree[p].push_back({q,r});
            tree[q].push_back({p,r});
        }

        findParentAndDis(1, -1, 0,0);
        
        //lca using dynamic programming, copied from topcoder
        //precomputing values
        for(i=1;i<=n;i++){
            for(j=1;1<<j<=n;j++){
                lca[i][j]=-1;
            }
        }
        
        for(i=1;i<=n;i++){
            lca[i][0]=parent[i];
        }
        
        for(j=1;1<<j<=n;j++){
            for(i=1;i<=n;i++){
                if(lca[i][j-1]!=-1){
                    lca[i][j]=lca[lca[i][j-1]][j-1];
                }
            }
        }
        //precomputation ends here
        
     //   cout<<lcaQuery(3, 6)<<endl;
     //   cout<<level[1]<<" "<<level[2]<<" "<<level[3]<<" "<<level[6]<<endl;
        
        k=0;
        chainNo=0;
        heavyLightDecomposition(1, -1, 0, 0);
        for(i=1;i<=k;i++){
            cout<<edgeStore[i]<<" ";
        }
        cout<<endl;
        solveByDFS(1, -1);
        for(i=1;i<=n;i++){
            cout<<ans[i]<<endl;
        }
  //      cout<<headOfNode[1]<<" "<<headOfNode[2]<<" "<<headOfNode[5]<<" "<<k<<" "<<chainNo<<endl;
        
    }
    
    return 0;
}


/*
notes:::
 
 not sure about accuracy yet
 
 
*/




#include "iostream"
#include "vector"
#include "map"
#include "climits"
#include "queue"
#include "algorithm"
#include "set"
#include "cmath"
#include "cstring"
#include "stack"

using namespace std;

long long i,j,k,l,n;
bool a[10];

int main(){
    
 //   freopen("/Users/ravikumar/documents/programming/codechef/codechef/A-large.in", "r", stdin);
 //   freopen("/Users/ravikumar/documents/programming/codechef/codechef/output.txt", "w", stdout);
    int t,ti=1;
    cin>>t;
    while(t--){
        scanf("%lld",&n);
        if(n==0){
            printf("Case #%d: INSOMNIA\n",ti);
            ti++;
            continue;
        }
        for(i=0;i<10;i++){
            a[i]=false;
        }
        long long ans=n;
        k=n;
        bool found=false;
        for(j=2;;j++){
            i=n;
       //     cout<<n<<endl;
            while(i){
                a[i%10]=true;
                i/=10;
            }
            found=true;
            for(i=0;i<10;i++){
                if(!a[i]){
                    found=false;
                    break;
                }
            }
            if(found){ans=n;break;}
            n=k*j;
            
        }
        printf("Case #%d: %lld\n",ti,ans);
        ti++;
    }
}