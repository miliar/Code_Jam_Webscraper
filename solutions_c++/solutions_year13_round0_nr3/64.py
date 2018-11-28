import java.io.*;
import java.util.*;
import java.math.*;

class Main
{

	public static String s1,s2;
	public static ArrayList <BigInteger> daftar;
	public static boolean palindrome(String x)
	{
		int i;
		for (i=0;i<x.length();++i)
		{
			if (x.charAt(i)!=x.charAt(x.length()-1-i))
				return false;
		}
		return true;
	}
	public static void bf(int x)
	{
		if (x==26)
			return;
		BigInteger lol,lol2;
		String slol,slol2;
		//genap
		slol=s1+s2;
		lol = new BigInteger(slol);
		lol2=lol.multiply(lol);
		slol2=lol2.toString();
		if (palindrome(slol2))
			daftar.add(lol2);
		//ganjil
		slol=s1+"0"+s2;
		lol = new BigInteger(slol);
		lol2=lol.multiply(lol);
		slol2=lol2.toString();
		if (palindrome(slol2))
			daftar.add(lol2);
		slol=s1+"1"+s2;
		lol = new BigInteger(slol);
		lol2=lol.multiply(lol);
		slol2=lol2.toString();
		if (palindrome(slol2))
			daftar.add(lol2);
		slol=s1+"2"+s2;
		lol = new BigInteger(slol);
		lol2=lol.multiply(lol);
		slol2=lol2.toString();
		if (palindrome(slol2))
			daftar.add(lol2);
		String olds1=s1;
		String olds2=s2;
		s1=olds1+"0";
		s2="0"+olds2;
		bf(x+1);
		s1=olds1+"1";
		s2="1"+olds2;
		bf(x+1);
	}
	public static void main(String[] args) throws IOException
	{
		int i;
		s1="1";
		s2="1";
		daftar=new ArrayList();
		bf(1);
		s1="2";
		s2="2";
		bf(1);
		Collections.sort(daftar);
		for (i=0;i<daftar.size();++i)
			System.out.println(daftar.get(i));
	}
}

class Reader
{
	private BufferedReader x;
	private StringTokenizer st;
	public Reader(InputStream in)
	{
		x = new BufferedReader (new InputStreamReader(in));
		st = null;
	}
	public String nextString() throws IOException
	{
		while (st == null || !st.hasMoreTokens())
			st=new StringTokenizer(x.readLine());
		return st.nextToken();
	}
	public int nextInt() throws IOException
	{
		return Integer.parseInt(nextString());
	}
	public double nextDouble() throws IOException
	{
		return Double.parseDouble(nextString());
	}
}