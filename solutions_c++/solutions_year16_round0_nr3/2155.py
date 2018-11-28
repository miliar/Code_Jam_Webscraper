import java.io.*;
import java.math.*;
import java.util.*;

public class Main 
{
	Scanner in;
	PrintWriter out;

	public static void main(String[] args) throws IOException 
	{
		new Main().run();
	}

	void run() throws IOException
	{
		in = new Scanner(System.in);
		out = new PrintWriter(System.out);
		solve();
		out.flush();
	}

	void solve() throws IOException
	{
		solve(32, 500);
	}

	void solve(int length, int count)
	{
		Random random = new Random(31415);

		out.println("Case #1:");
		HashSet<String> used = new HashSet<>();
		for (int it = 0; it < count; it++)
		{
			//System.err.println(it);
			//System.err.flush();

			while (true)
			{
				String str = genRandString(length, random);

				if (used.contains(str))
					continue;
				used.add(str);

				ArrayList<Integer> divisors = check(str);
				if (divisors == null)
					continue;

				out.print(str);
				for (int i = 0; i < divisors.size(); i++)
					out.print(" " + divisors.get(i));
				out.println();
				break;
			}
		}
	}

	String genRandString(int length, Random random)
	{
		StringBuilder result = new StringBuilder();
		for (int i = 0; i < length; i++)
			result.append((char)('0' + Math.abs(random.nextInt()) % 2));
		return result.toString();
	}

	ArrayList<Integer> check(String str)
	{
		int n = str.length();
		if (str.charAt(0) != '1' || str.charAt(n - 1) != '1')
			return null;
		ArrayList<Integer> result = new ArrayList<Integer>();
		for (int base = 2; base <= 10; base++)
		{
			BigInteger number = new BigInteger(str, base);
			Integer divisor = getDivisor(number);
			if (divisor == null)
				return null;
			result.add(divisor);
		}
		return result;
	}

	Integer getDivisor(BigInteger number)
	{
		if (number.isProbablePrime(100))
			return null;
		for (int i = 2; i <= 300000; i++)
		{
			if (number.equals(BigInteger.valueOf(i)))
				throw new Error("");
			if (number.mod(BigInteger.valueOf(i)).equals(BigInteger.ZERO))
				return i;
		}
		return null;
	}
}


